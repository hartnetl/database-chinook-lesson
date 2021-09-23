from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
# base is imported above and contains the meta data from our database and is mapped here
base = declarative_base()


# We're gonna create a new table
# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# create a new instance of sessionmaker and point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
# note the lowercase s
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# NOW LETS ADD OUR ENTRIES

# creating records on our Progammer table
# each entry is using the person's name as thr variable name
ada_lovelace = Programmer(
    # the worlds first programmer
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    # invented software engineering
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

laura_hartnett = Programmer(
    first_name="Laura",
    last_name="Hartnett",
    gender="F",
    nationality="Irish",
    famous_for="Being weird and cheerful"
)

# add each instance of our programmers to our session
# MAKE SURE TO ONLY ADD EACH PERSON ONCE
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
session.add(laura_hartnett)

# commit our session to the database
session.commit()


# query the database to find all Programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        # this combines the first and last name
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )