from models import Barber, Client, Appointment
from simple_term_menu import TerminalMenu
from prettycli import red, blue, green
import re


class Bookit:
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
        exp = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        if email == "exit":
            self.start()
        if re.fullmatch(exp, email):
            pass
        else:
            print(red("email address is not valid\n"))
            self.barber()


cli = Bookit()
cli.start()
