import re
from datetime import datetime
from prettycli import red, blue, green

exp = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"


def get_email(message):
    print(green(f"\n{message}\n"))
    email = input()
    if email == "exit":
        return None

    if re.fullmatch(exp, email):
        return email
    else:
        print(red("\nemail address is not valid\n"))
        return get_email(message)


def get_date(message):
    print(f"\n{message}\n")
    date_string = input()
    if date_string == "exit":
        return None
    try:
        date = datetime.strptime(date_string, "%Y-%m-%d").date()
        return date
    except ValueError:
        print(red("\ndate is not valid\n"))
        return get_date(message)


def get_time(message):
    print(f"\n{message}\n")
    time_string = input()
    if time_string == "exit":
        return None

    try:
        time = datetime.strptime(time_string, "%I:%M %p").time()
        return time
    except ValueError:
        print(red("\ntime is not valid\n"))
        return get_time(message)
