from models import Barber, Client, Appointment
from simple_term_menu import TerminalMenu
from prettycli import red, blue, green
import re
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from datetime import datetime, date, time
from prettytable import PrettyTable

engine = create_engine("sqlite:///bookit.db")
session = Session(engine)


class Bookit:
    def __init__(self):
        self.user = None

    def start(self):
        print(green("\nWelcome to our barber shop\n"))
        print("Are you a barber or a client?\n")
        options = ["Barber", "Client", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if menu_entry_index == 0:
            self.barber()
        if menu_entry_index == 1:
            self.client()
        if menu_entry_index == 2:
            self.exit()

    def barber(self):
        message = "Please enter your email address. type exit to go back"
        email = self.get_email(message)
        if email == None:
            self.start()
            return
        self.handle_barber_login(email)

    def handle_barber_login(self, email):
        barber = Barber.find_barber_by_email(session, email)
        if not barber:
            print(red("email address doesn't exist\n"))
            self.barber()
        else:
            self.user = barber
            self.barber_page()

    def barber_page(self):
        print(green(f"\nWelcome {self.user.first_name}\n"))
        print("what would you like to do?")
        options = [
            "See your booked appointments",
            "Add appointments",
            "See you Stats",
            "Exit",
        ]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()

        if menu_index == 0:
            self.see_appointments()

        if menu_index == 1:
            self.add_appointments()
        if menu_index == 2:
            self.see_stats()

        if menu_index == 3:
            self.exit()

    def see_appointments(self):
        message = "Enter Start Date (format yyyy-mm-dd): (type exit to go back)"
        sdate = self.get_date(message)
        if sdate == None:
            self.barber_page()
            return

        message = "Enter End Date: (format yyyy-mm-dd) (type exit to go back)"
        edate = self.get_date(message)
        if edate == None:
            self.barber_page()
            return

        booked_appointments = Appointment.find_appointments(
            session,
            barber_id=self.user.id,
            start_date=sdate,
            end_date=edate,
            booked=True,
        )
        if not booked_appointments:
            print("\nNo booked appointments\n")
        else:
            for appointment in booked_appointments:
                print(
                    f"\nAppointment with {appointment.client} on {appointment.date} at {appointment.time.strftime('%I:%M %p')}"
                )
        self.barber_page()

    def get_email(self, message):
        print(green(f"\n{message}\n"))
        email = input()
        if email == "exit":
            return None

        exp = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        if re.fullmatch(exp, email):
            return email
        else:
            print(red("\nemail address is not valid\n"))
            return self.get_email(message)

    def get_date(self, message):
        print(f"\n{message}\n")
        date_string = input()
        if date_string == "exit":
            return None
        try:
            date = datetime.strptime(date_string, "%Y-%m-%d").date()
            return date
        except ValueError:
            print(red("\ndate is not valid\n"))
            return self.get_date(message)

    def get_time(self, message):
        print(f"\n{message}\n")
        time_string = input()
        if time_string == "exit":
            return None

        try:
            time = datetime.strptime(time_string, "%I:%M %p").time()
            return time
        except ValueError:
            print(red("\ntime is not valid\n"))
            return self.get_time(message)

    def add_appointments(self):
        message = "Enter appointment date: (format yyyy-mm-dd) (type exit to go back)"
        date = self.get_date(message)
        if date == None:
            self.barber_page()
            return

        message = "Enter appointment time: (format hh:00 AM/PM)"
        time = self.get_time(message)
        if time == None:
            self.barber_page()
            return

        appointment = self.user.add_appointment(date, time, session)
        if appointment:
            print("\nAppointment added successfully\n")
            self.barber_page()

    def see_stats(self):
        start_date = date(datetime.now().year, 1, 1)
        end_date = datetime.now().date()
        # get all appointments YTD
        appointments = Appointment.find_appointments(
            session=session,
            barber_id=self.user.id,
            start_date=start_date,
            end_date=end_date,
            booked=True,
        )

        count = {}
        for appointment in appointments:
            month = appointment.date.strftime("%b")
            count[month] = count.get(month, 0) + 1
        x = PrettyTable()
        x.field_names = ["Month", "Number of Booked Appointments"]
        for key, value in count.items():
            x.add_row([key, value])
        print(green("\nYour stats YTD:\n"))
        print(x)
        self.barber_page()

    def exit(self):
        print("\nBye\n")

    def client(self):
        print("\n New or Existing client?\n")
        options = ["New Client", "Returning Client", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if menu_entry_index == 0:
            self.new_client()
        if menu_entry_index == 1:
            self.client_login()
        if menu_entry_index == 2:
            self.exit()

    def new_client(self):
        message = "Please Enter yor email: (type exit to go back)"
        email = self.get_email(message)
        if email == None:
            self.client()
            return

        first_name = input("\nPlease Enter First Name: (type exit to go back): ")
        if first_name == "exit":
            self.client()
            return
        last_name = input("\nPlease Enter Last Name: ")
        if last_name == "exit":
            self.client()
            return
        self.handle_client_signup(first_name, last_name, email)

    def handle_client_signup(self, first_name, last_name, email):
        client = Client(first_name=first_name, last_name=last_name, email=email)
        session.add(client)
        session.commit()
        self.user = client
        self.client_page()

    def client_page(self):
        print(green(f"\nWelcome {self.user.first_name}\n"))
        print("what would you like to do?")
        options = [
            "See your upcoming appointments",
            "book an appointment",
            "Exit",
        ]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()

        if menu_index == 0:
            self.upcoming_appointments()

        if menu_index == 1:
            self.book_appointment()

        if menu_index == 2:
            self.exit()

    def upcoming_appointments(self):
        start_date = datetime.now().date()
        appointments = Appointment.find_appointments(
            session=session, client_id=self.user.id, start_date=start_date
        )
        if not appointments:
            print("\n you have no upcoming appointments\n")

        else:
            for appointment in appointments:
                print(
                    f"\nAppointment with {appointment.barber} on {appointment.date} at {appointment.time.strftime('%I:%M %p')}\n"
                )

        self.client_page()

    def book_appointment(self):
        message = "Enter Start Date (format yyyy-mm-dd): (type exit to go back)"
        sdate = self.get_date(message)
        if sdate == None:
            self.client_page()
            return

        message = "Enter End Date: (format yyyy-mm-dd) (type exit to go back)"
        edate = self.get_date(message)
        if edate == None:
            self.client_page()
            return

        unbooked_appointments = Appointment.find_appointments(
            session,
            start_date=sdate,
            end_date=edate,
            booked=False,
        )
        if not unbooked_appointments:
            print("\n no available appointments with these dates\n")
            self.book_appointment()
            return
        options = ["Exit"] + list(map(Bookit.print_appointment, unbooked_appointments))
        print("\n please choose an appointment:\n")
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()
        if menu_index == 0:
            self.book_appointment()
        else:
            appointment = unbooked_appointments[menu_index - 1]
            self.user.book_appointment(session=session, appointment=appointment)
            print("\nappointment booked successfully\n")
            self.client_page()

    @staticmethod
    def print_appointment(appointment):
        return f"{appointment.barber} on {appointment.date} at {appointment.time.strftime('%I:%M %p')}"

    def client_login(self):
        message = "Please enter your email address. type exit to go back"
        email = self.get_email(message)
        if email == None:
            self.client_page()
            return
        client = Client.find_client_by_email(session, email)
        if not client:
            print(red("\nemail address doesn't exist\n"))
            self.client()
        else:
            self.user = client
            self.client_page()


cli = Bookit()
cli.start()
