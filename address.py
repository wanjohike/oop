from CustomerSystem import Person, Address, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

cust1 = Person(name ='Bronson Loni', age=24)
cust2 = Person(name='Hayan Mohamed', age=23)

cust1.addresses = [
    Address(email = 'lonithebron@gmail.com'),
    Address(email='hloni@gmail.com'),
]

# append the addresses to the specific customer
cust1.addresses.append(Address(email = 'bron@mail.com'))

# use the sessionmaker to add the data into our database
session.add(cust1)
session.add(cust2)

# run commit to save to the database

session.commit()

cust1 = session.query(Person).filter(Person.name.like('Bro%')).first

print(cust1,cust1.addresses)

def disp_info():
    addresses = session.query((Address)).all()

    for address in addresses:
        print(f'{address.person.name}<{address.email}>')
