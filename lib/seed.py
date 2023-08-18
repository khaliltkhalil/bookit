#!/usr/bin/env python3

from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import Session
from faker import Faker
from models import Barber, Client, Appointment


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
        email = first_name + last_name + "@" + "gmail.com"
        barber = Barber(first_name=first_name, last_name=last_name, email=email)
        barbers.append(barber)
    session.add_all(barbers)
    session.commit()
    return barbers


if __name__ == "__main__":
    with Session(engine) as session:
        clear_db()
        populate_barbers()
        # barbers = populate_barbers()
