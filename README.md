# Bookit

A CLI application to manage online booking.

## Installation

Fork and clone the repository to your local machine.

Install dependencies :

```bash
pipenv install
```

Move to the virtual environment :

```bash
pipenv shell
```

Make sure you are in the lib subfolder :

```bash
cd lib
```

Run the database migration :

```bash
alembic upgrade head
```

Seed the database :

```bash
python seed.py
```

Run the application :

```bash
python bookit.py
```

## Usage

When you run the application you can choose to log in as a barber or a client.

As a barber you can:

1. See upcoming booked appointment
2. Add availability
3. See your stats which is the number of booked appointment per month year to date.

As a client you can :

1. See upcoming appointments
2. Book an appointment

![](https://github.com/khaliltkhalil/bookit/blob/main/Bookit_Demo.gif))

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
