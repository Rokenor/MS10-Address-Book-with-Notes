import sys
from . import validators
from .classes import AddressBook, Record

def close(args = None, book = None):
    """Exit the program"""
    print("Good bye!")
    sys.exit(0)

def command_list(args = None, book = None):
    """Prints a list of available commands."""
    return (
        "Available commands:\n"
        "- hello: Greet the user\n"
        "- add <name> <phone>: Add a new contact\n"
        "- add-address <name> <address>: Add an address to a contact\n"
        "- add-birthday <name> <birthday>: Add a birthday to a contact\n"
        "- add-email <name> <email>: Add an email address to a contact\n"
        "- all: List all contacts\n"
        "- search <name>: Find a contact by name\n"
        "- birthdays <days>: List upcoming birthdays in the next <days> days\n"
        "- change <name> <new_phone>: Change an existing contact's phone\n"
        "- show-birthday <name>: Show a contact's birthday\n"
        "- close or exit: Exit the program\n"
    )

@validators.add_contact_validator
def add_contact(args, book: AddressBook):
    """Adds a new contact to the address book."""
    name, phone = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

def add_address(args, book: AddressBook):
    """Adds an address to a contact in the address book."""
    name = args[0]
    address = " ".join(args[1:])
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.add_address(address)
    return "Address added."

@validators.list_contacts_validator
def list_contacts(_, book: AddressBook):
    """Returns a string containing all contacts in the address book."""
    return "\n".join(f"{rec}" for rec in book.values())

@validators.find_contact_validator
def find_contact(args, book: AddressBook):
    """Finds a contact by name and returns a string representation of the contact."""
    name = args[0]
    rec = book.find(name)
    return f"{rec}" if rec else "Contact not found."

@validators.change_contact_validator
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    rec = book.find(name)
    if rec is None:
        return "Contact not found."
    
    rec.edit_phone(old_phone, new_phone)
    return "Contact updated."

@validators.add_birthday_validator
def add_birthday(args, book: AddressBook):
    """Adds a birthday to a contact in the address book."""
    name, birthday = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    
    record.add_birthday(birthday)
    return "Birthday added."

@validators.show_birthday_validator
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    return f"{name}'s birthday is {record.birthday}."

@validators.birthdays_validator
def birthdays(args, book: AddressBook):
    """Returns a list of users who need to be greeted on the next week"""
    upcoming_days = int(args[0])
    birthdays_list = book.get_upcoming_birthdays(upcoming_days)
    if not birthdays_list:
        return "No upcoming birthdays."
    return "\n".join(f"{record.name}: {record.birthday}" for record in birthdays_list)

def add_email(args, book: AddressBook):
    """Adds an email address to a contact in the address book."""
    name, email = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.add_email(email)
    return "Email added."
