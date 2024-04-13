#!/usr/bin/python3
"""script that lists all State objects from the database"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    if len(sys.argv) == 5:
        state_name = sys.argv[4]
    instances = []
    instances = [instance[0] for instance in session.query(State.id, State.name)
                .filter(State.name == state_name)]
    if len(instances) > 0:
        for instance in instances:
            print(instance)
    else:
        print("Not found")