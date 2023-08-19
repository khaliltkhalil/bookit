#!/usr/bin/env python3
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models import Barber, Client, Appointment
import ipdb
import datetime

engine = create_engine("sqlite:///bookit.db")

if __name__ == "__main__":
    session = Session(engine)
    barber = session.execute(select(Barber)).scalars().first()
    ipdb.set_trace()
