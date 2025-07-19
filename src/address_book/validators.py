import re
from functools import wraps
from src.address_book.classes import AddressBook, Record
from colorama import Fore, init
init(autoreset=True)

def parse_input_validator(func):
    """Validator for parsing user input."""
    @wraps(func)
    def wrapper(user_input):
        if not user_input:
            return Fore.RED + "Invalid input. Please enter a command."
        return func(user_input)
    return wrapper

def add_contact_validator(func):
    """Validator for adding a contact."""
    @wraps(func)
    def wrapper(args, contacts):
        if len(args) != 2:
            return Fore.RED + "Invalid number of arguments. Usage: add <name> <phone>"
        name, *phone = args
        phone = "".join(phone)

        if not name or not phone:
            return Fore.RED + "Name and phone cannot be empty."

        if not _is_phone(phone):
            return Fore.RED + "Invalid phone number."

        return func(args, contacts)
    return wrapper

def add_address_validator(func):
    """Validator for adding an address to a contact."""
    @wraps(func)
    def wrapper(args, book: AddressBook):
        if len(args) < 2:
            return Fore.RED + "Invalid number of arguments. Usage: add-address <name> <address>"
        name = args[0]
        if not name:
            return Fore.RED + "Name cannot be empty."
        return func(args, book)
    return wrapper

def list_contacts_validator(func):
    """Validator for listing contacts."""
    @wraps(func)
    def wrapper(args, book: AddressBook):
        if not isinstance(book, AddressBook) or not book.data:
            return Fore.RED + "No contacts found."
        return func(args, book)
    return wrapper

def find_contact_validator(func):
    """Validator for finding a contact."""
    @wraps(func)
    def wrapper(args, contacts):
        if len(args) != 1:
            return Fore.RED + "Invalid number of arguments. Usage: find <name>"
        return func(args, contacts)
    return wrapper

def delete_contact_validator(func):
    """Validator for deleting a contact."""
    @wraps(func)
    def wrapper(args, contacts):
        if len(args) != 1:
            return Fore.RED + "Invalid number of arguments. Usage: delete <name>"
        return func(args, contacts)
    return wrapper

def edit_address_validator(func):
    """Validator for editing a contact's address."""
    @wraps(func)
    def wrapper(args, book: AddressBook):
        if len(args) < 2:
            return Fore.RED + "Invalid number of arguments. Usage: edit-address <name> <new_address>"
        name = args[0]
        if not name:
            return Fore.RED + "Name cannot be empty."
        return func(args, book)
    return wrapper

def edit_phone_validator(func):
    """Validator for editing a contact's phone number."""
    @wraps(func)
    def wrapper(args, contacts):
        if len(args) != 3:
            return Fore.RED + "Invalid number of arguments. Usage: edit-phone <name> <old_phone> <new_phone>"

        _, old_phone, *new_phone = args
        new_phone = "".join(new_phone)

        if not _is_phone(new_phone):
            return Fore.RED + "Invalid phone number."

        return func(args, contacts)

    return wrapper

def add_birthday_validator(func):
    """Validator for adding a birthday to a contact."""
    @wraps(func)
    def wrapper(args, book: AddressBook):
        if len(args) != 2:
            return Fore.RED + "Invalid number of arguments. Usage: add_birthday <name> <birthday>"
        if not isinstance(book, AddressBook):
            return Fore.RED + "Invalid address book instance."

        name, birthday = args
        if not name or not birthday:
            return Fore.RED + "Name and birthday cannot be empty."

        r = Record('')
        try:
            r.add_birthday(birthday)
        except ValueError as e:
            return Fore.RED + str(e)

        return func(args, book)
    return wrapper

def birthdays_validator(func):
    """Validator for listing upcoming birthdays."""
    @wraps(func)
    def wrapper(args, book: AddressBook):
        if not isinstance(book, AddressBook):
            return Fore.RED + "Invalid address book instance."
        return func(args, book)
    return wrapper

def add_email_validator(func):
    """Validator for adding an email to a contact."""
    @wraps(func)
    def wrapper(args, book: AddressBook):
        if len(args) != 2:
            return Fore.RED + "Invalid number of arguments. Usage: add-email <name> <email>"
        name, email = args
        if not name or not email:
            return Fore.RED + "Name and email cannot be empty."

        if not _is_email(email):
            return Fore.RED + "Invalid email."

        return func(args, book)
    return wrapper

def edit_email_validator(func):
    """Validator for editing a contact's email."""
    @wraps(func)
    def wrapper(args, book: AddressBook):
        if len(args) != 2:
            return Fore.RED + "Invalid number of arguments. Usage: edit-email <name> <new_email>"
        name, new_email = args
        if not name or not new_email:
            return Fore.RED + "Name and new email cannot be empty."

        if not _is_email(new_email):
            return Fore.RED + "Invalid email."

        return func(args, book)
    return wrapper


def _is_email(email):
    return re.match(r"[^@ \"(),:;<>\[\\\]]+@[^@ \"(),:;<>\[\\\]]+\.[^@ \"(),:;<>\[\\\]]+", email)

def _is_phone(new_phone):
    return re.match(r"^\+?\(?[0-9]{3}\)?[-\s.]?[0-9]{2,3}[-\s.]?[0-9]{2,6}[-\s.]??[0-9]{2,6}$", new_phone)
