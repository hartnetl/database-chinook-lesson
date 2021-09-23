# Just told to import create_engine to Metadata at the start
from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
# /// means chinook is hosted locally within the workspace environment
db = create_engine("postgresql:///chinook")

# The MetaData class will contain data about our tables, and the data about the data in those tables
meta = MetaData(db)

# Create the schema / data models for the tables you need
# We're gonna use the same 6 as we did for the previous chinook lesson

# create variable for "Artist" table
# This is using the table imported above
artist_table = Table(
    "Artist", meta,
    # The column name is easiest gotten using the 
    # SELECT * FROM "Artist" WHERE false; command
    # Then enter the type of data per column
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    # The album is the primary key for this table, but it links to the artist table.
    # The foregin key must point to the related table and the id column
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    # media type is technically a foreign key, but we don't need it for our queries
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    # Floats use decimal points
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection: