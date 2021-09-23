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

class Places(base):
    __tablename__ = "Places"
    id = Column(Integer, primary_key=True)
    place_name = Column(String)
    country_name = Column(String)
    year = Column(Integer)
    Revisit = Column(String)


# create a new instance of sessionmaker and point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
# note the lowercase s
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# NOW LETS ADD OUR ENTRIES

# PROGRAMMER TABLE

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
# session.add(laura_hartnett)

# commit our session to the database
# session.commit()

# MY PLACES TABLE

lisbon = Places(
    place_name = "Lisbon",
    country_name = "Portugal",
    year = "2016",
    Revisit = "y"
)

shanghai = Places(
    place_name = " Shanghai ",
    country_name = "China",
    year = "2018",
    Revisit = "n"
)

abu_dhabi = Places(
    place_name = "Abu Dhabi ",
    country_name = " UAE",
    year = "2018",
    Revisit = "y"
)

brisbane = Places(
    place_name = "Brisvegas",
    country_name = "Australia",
    year = "2017",
    Revisit = "y"
)

# session.add(lisbon)
# session.add(shanghai)
# session.add(brisbane)
# session.add(abu_dhabi)

# session.commit()



# SECOND PART OF THE LESSON - UPDATE AND DELETE

################
### updating ###
################

# updating a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# filter by primary key of IDs is the best way to find unique values. Make sure to add .first()
# The below line updates our famous for entry
# programmer.famous_for = "World President"

# commit our session to the database
# session.commit()

# UPDATE MY EXAMPLE
# place = session.query(Places).filter_by(id=2).first()
# place.place_name = "Shanghai"
# session.commit()

# updating my multiple

# places = session.query(Places)
# for place in places:
#     if place.Revisit.lower() == "y":
#         place.Revisit = "Y"
#     elif place.Revisit.lower() == "n":
#         place.Revisit = "N"
#     else: 
#         print("Did you enter that correctly?")

# DON'T FORGET TO COMMENT OUT YOUR ALREADY USED CODE SO YOU DON'T REENTER IT

# updating multiple records - every person in the records of Programmer
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()
    # the commit needs to be part of the loop

##############
###deleting###
##############

# deleting a single record

# You can't always view the unique ID, so you can prompt to find the full name required

# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()

# defensive programming
# if programmer is not None:
    # if a match is found, make sure they want to delete it 
    # print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
    # confirmation = input("Are you sure you want to delete this record? (y/n) ")
    # if confirmation.lower() == "y":
    #     session.delete(programmer)
    #     session.commit()
    #     print("Programmer has been deleted")
    # here they don't want to delete it
    # else:
    #     print("Programmer not deleted")
# else:
    # no match found
    # print("No records found")


# DELETING ONE OF MY PLACE ENTRIES

location = input("What country are you looking for? ")
place = session.query(Places).filter_by(country_name=location).first()

if place is not None:
    print(f"Place Found: {location}")
    confirmation = input("Are you sure you want to delete this record? (y/n) ")
    if confirmation.lower() == "y":
        session.delete(place)
        session.commit()
        print("Place has been deleted")
    else:
        print("Place not deleted")
else:
    print("No records found")




# delete multiple/all records in Programmer
# Always use defensive programming to confirm what it is you're about to delete
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()


# query the database to find all Programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         # this combines the first and last name
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep=" | "
#     )

places = session.query(Places)
for place in places:
    print(
        place.id,
        # this combines the first and last name
        place.place_name,
        place.country_name,
        place.year,
        place.Revisit,
        sep=" | "
    )