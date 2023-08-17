from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Time, DateTime, Integer, String, Boolean, ForeignKey


Base = declarative_base()


class Barber(Base):
    __tablename__ = "barbers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"Barber {self.first_name} {self.last_name}"


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"Client {self.first_name} {self.last_name}"


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    barber_id = Column(Integer, ForeignKey("barbers.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))
    date = Column(DateTime, nullable=False)
    time = Column(Time, nullable=False)
    booked = Column(Boolean, default=False)

    def __repr__(self):
        return (
            f"Appointment {self.barber_id} with {self.client_id}"
            + f"on {self.date} at {self.time}"
        )
