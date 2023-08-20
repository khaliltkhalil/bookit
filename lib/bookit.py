from models import Barber, Client, Appointment
from simple_term_menu import TerminalMenu
from prettycli import red, blue, green
import re
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

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

    def barber(self):
        print(green("\nPlease enter your email address. type exit to go back\n"))
        email = input()

        if email == "exit":
            self.start()

        exp = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        if re.fullmatch(exp, email):
            self.handle_barber_login(email)
        else:
            print(red("email address is not valid\n"))
            self.barber()

    def handle_barber_login(self, email):
        barber = Barber.find_barber_by_email(session, email)
        if not barber:
            print(red("email address doesn't exist\n"))
            self.barber()
        self.user = barber
        self.barber_page()

    def barber_page(self):
        print(green(f"\nWelcome {self.user.first_name}\n"))
        print("what would you like to do?")


cli = Bookit()
cli.start()
