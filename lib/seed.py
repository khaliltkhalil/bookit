#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine("sqlite:///bookit.db")

if __nme__ == "__main__":
    with Session(engine) as session:
        pass
