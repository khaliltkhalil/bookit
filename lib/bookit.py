from models import Barber, Client, Appointment
from simple_term_menu import TerminalMenu
from prettycli import red, blue, green


class Bookit:
    def start(self):
        print(green("\nWelcome to our barber shop\n"))
        print("Are you a barber or a client?\n")
        options = ["Barber", "Client", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")


cli = Bookit()
cli.start()
