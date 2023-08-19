from sqlalchemy.orm import declarative_base, Relationship
from sqlalchemy import Column, Time, Date, Integer, String, Boolean, ForeignKey, select


Base = declarative_base()


class Barber(Base):
    __tablename__ = "barbers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

    appointments = Relationship("Appointment", back_populates="barber")

    def __repr__(self):
        return f"Barber {self.first_name} {self.last_name}"

    # create an appointment ,  day and time are python object
    def add_appointment(self, date, time, session):
        appointment = Appointment(date=date, time=time)
        appointment.barber = self
        session.add(appointment)
        session.commit()

    # get all appointments between certain dates
    def get_appointments(
        self,
        session,
        start_date=None,
        end_date=None,
        start_time=None,
        end_time=None,
        booked=None,
    ):
        stm = select(Appointment).filter_by(barber_id=self.id)
        if start_date:
            stm = stm.filter(Appointment.date >= start_date)

        if end_date:
            stm = stm.filter(Appointment.date <= end_date)

        if start_time:
            stm = stm.filter(Appointment.time >= start_time)

        if start_time:
            stm = stm.filter(Appointment.time <= end_time)

        if booked != None:
            stm = stm.filter(Appointment.booked == booked)

        appointments = session.execute(stm).scalars().all()

        return appointments


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

    appointments = Relationship("Appointment", back_populates="client")

    def __repr__(self):
        return f"Client {self.first_name} {self.last_name}"


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    barber_id = Column(Integer, ForeignKey("barbers.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    booked = Column(Boolean, default=False)

    barber = Relationship("Barber", back_populates="appointments")
    client = Relationship("Client", back_populates="appointments")

    def __repr__(self):
        return (
            f"Appointment {self.barber_id} with {self.client_id}"
            + f"on {self.date} at {self.time}"
        )
