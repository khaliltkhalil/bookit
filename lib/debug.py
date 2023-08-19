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
    sdate = datetime.date(2023, 8, 24)
    edate = datetime.date(2023, 8, 25)
    stime = datetime.time(9)
    etime = datetime.time(18)
    appointments = barber.get_appointments(session, sdate, edate, stime, etime, False)
    ipdb.set_trace()
