#!/usr/bin/python3
"""prints all City objects"""
from model_city import City
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    my_tuple = (State.name, City.id, City.name)
    for instance in session.query(my_tuple).filter(State.id == City.state_id):
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])

    session.close()