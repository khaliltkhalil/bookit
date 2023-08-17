from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Time, Date, Integer, String


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
