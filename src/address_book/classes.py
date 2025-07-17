from collections import UserDict
from datetime import datetime, timedelta

class Field:
    """Base class for fields in the address book."""
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """Represents a person's name in the address book."""

class Address(Field):
    """Represents an address in the address book."""
    def __init__(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Address must be a string")
        super().__init__(value)

class Phone(Field):
    """Represents a phone number in the address book."""
    def __init__(self, value: str):
        if len(value) != 10 or not value.isdigit():
            raise ValueError(f"Phone must be 10 digits long and contain only digits. Got: {value}")
        super().__init__(value)

class Email(Field):
    """Represents an email address in the address book."""
    def __init__(self, value):
        if "@" not in value:
            raise ValueError("Email must contain an '@' symbol. Got: " + value)
        super().__init__(value)

class Birthday(Field):
    """Represents a birthday in the address book."""
    def __init__(self, value: str):
        try:
            if not isinstance(value, str):
                raise ValueError("Birthday must be a string in the format DD.MM.YYYY")
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError as e:
            raise ValueError("Invalid date format. Use DD.MM.YYYY") from e
        super().__init__(value)

class Record:
    """
    Represents a record in the address book.

    Attributes:
        name (Name): The name of the record.
        address (Address): The address of the record.
        birthday (Birthday): The birthday of the record.
        phones (list[Phone]): A list of phone numbers associated with the record.
        email (Email): The email address of the record.
    """
    def __init__(self, name: str):
        self.name = Name(name)
        self.address = Address | None
        self.birthday: Birthday | None = None
        self.phones = []
        self.email = Email | None

    def add_address(self, address: str):
        """Adds an address to the record."""
        self.address = Address(address)

    def show_address(self) -> str:
        """Returns the address of the record."""
        return getattr(self.address, 'value', "Not set")

    def add_birthday(self, birthday: str):
        """Adds a birthday to the record."""
        self.birthday = Birthday(birthday)

    def show_birthday(self) -> str:
        """Returns the birthday of the record."""
        if self.birthday:
            return self.birthday.value
        return "Not set"

    def add_phone(self, phone: str):
        """Adds a phone number to the record."""
        self.phones.append(Phone(phone))

    def edit_address(self, new_address: str):
        """Edits the address of the record."""
        if self.address is None:
            self.address = Address(new_address)
        else:
            self.address.value = new_address

    def edit_phone(self, old_phone: str, new_phone: str):
        """Edits a phone number in the record."""
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                break

    def find_phone(self, phone: str) -> Phone | None:
        """Finds a phone number in the record."""
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone: str):
        """Removes a phone number from the record."""
        self.phones = [p for p in self.phones if p.value != phone]

    def add_email(self, email: str):
        """Adds an email address to the record."""
        self.email = Email(email)

    def show_email(self) -> str:
        """Returns the email of the record."""
        return getattr(self.email, 'value', "Not set")

    def edit_email(self, new_email: str):
        """Edits the email address of the record."""
        if self.email is None:
            self.email = Email(new_email)
        else:
            self.email.value = new_email

    def __str__(self):
        return (
            f"Name: {self.name.value}, "
            f"Birthday: {self.show_birthday()}, "
            f"Phones: {'; '.join(p.value for p in self.phones)}, "
            f"Address: {self.show_address()}, "
            f"Email: {self.show_email()}"
        )

class AddressBook(UserDict):
    """
    Represents an address book that stores records of individuals.

    The address book provides methods to add, find, and delete records.
    It also provides a method to get a list of records with upcoming birthdays.

    Attributes:
        data (dict[str, Record]): A dictionary that stores the records in the address book.
    """
    data: dict[str, Record]

    def add_record(self, record: Record):
        """Adds a record to the address book."""
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        """Finds a record in the address book by name."""
        return self.data.get(name)

    def delete(self, name: str) -> None:
        """Deletes a record from the address book."""
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(
            self,
            upcoming_days: int = 7,
            today: datetime = datetime.now()
        ) -> list[Record]:
        """Returns a list of records with upcoming birthdays by the given number of days."""
        if not isinstance(today, datetime):
            raise ValueError("Today must be a datetime object got: " + type(today))
        if not isinstance(upcoming_days, int) or upcoming_days < 0:
            raise ValueError("Upcoming days must be a non-negative integer. Got: " + str(upcoming_days))
        if len(self.data) == 0:
            return []

        upcoming_date = today.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=upcoming_days)

        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday is not None:
                bday_date = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                bday_this_year = bday_date.replace(year=today.year)
                birthday_diff = (upcoming_date.date() - bday_this_year).days
                if 0 <= birthday_diff <= upcoming_days:
                    upcoming_birthdays.append(record)
        return upcoming_birthdays
