#!/usr/bin/env python3

from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import Session
from faker import Faker
from models import Barber, Client, Appointment
import datetime
import random


engine = create_engine("sqlite:///bookit.db")
fake = Faker()


def clear_db():
    session.execute(delete(Barber))
    session.execute(delete(Client))
    session.execute(delete(Appointment))
    session.commit()


def populate_barbers():
    barbers = []
    for _ in range(5):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = first_name.lower() + last_name.lower() + "@" + "gmail.com"
        barber = Barber(first_name=first_name, last_name=last_name, email=email)
        barbers.append(barber)
    session.add_all(barbers)
    session.commit()
    return barbers


def populate_clients():
    clients = []
    for _ in range(50):
        first_name = fake.first_name_male()
        last_name = fake.last_name()
        email = first_name.lower() + last_name.lower() + "@" + "gmail.com"
        client = Client(first_name=first_name, last_name=last_name, email=email)
        clients.append(client)
    session.add_all(clients)
    session.commit()
    return clients


def populate_appointments(barbers):
    year = 2023
    appointments = []
    # booked appointments
    for month in range(1, 9):
        for day in range(1, 28):
            for time in range(8, 19):
                date = datetime.date(year, month, day)
                time = datetime.time(time)
                appointment = Appointment(date=date, time=time)
                appointment.barber = random.choice(barbers)
                appointment.client = random.choice(clients)
                appointment.booked = True
                appointments.append(appointment)
    session.add_all(appointments)
    session.commit()

    appointments = []
    # unbooked appointments
    month = 9
    for day in range(1, 30):
        for time in range(8, 19):
            date = datetime.date(year, month, day)
            time = datetime.time(time)
            appointment = Appointment(date=date, time=time)
            appointment.barber = random.choice(barbers)
            appointments.append(appointment)

    session.add_all(appointments)
    session.commit()


if __name__ == "__main__":
    with Session(engine) as session:
        clear_db()
        barbers = populate_barbers()
        clients = populate_clients()
        appointments = populate_appointments(barbers)
