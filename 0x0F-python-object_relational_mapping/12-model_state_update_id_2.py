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

    instances = [instance for instance in session.
                 query(State).filter(State.name.ilike('%a%')).all()]
    for instance in instances:
        if instance:
            session.delete(instance)
            session.commit()

    session.close()
