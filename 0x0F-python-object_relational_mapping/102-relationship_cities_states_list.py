#!/usr/bin/python3
"""prints all City objects"""
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import create_engine
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        for city in instance.cities:
            print(f"{city.id}: {city.name} -> {instance.name}")
    session.close()
