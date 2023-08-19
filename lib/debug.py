#!/usr/bin/env python3
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models import Barber, Client, Appointment
import ipdb
import datetime

engine = create_engine("sqlite:///bookit.db", echo=True)

if __name__ == "__main__":
    session = Session(engine)
    barber = session.execute(select(Barber)).scalars().first()
    barber_fname = "Kathryn"
    sdate = datetime.date(2023, 8, 24)
    edate = datetime.date(2023, 8, 25)
    stime = datetime.time(9)
    etime = datetime.time(18)
    appointments = Appointment.find_appointments(
        session,
        barber_first_name=barber_fname,
        start_date=sdate,
        end_date=edate,
        start_time=stime,
        end_time=etime,
        booked=False,
    )

    client = Client.find_client_by_email(session, "patrickdennis@gmail.com")
    client.book_appointment(session, appointments[0])
    ipdb.set_trace()
