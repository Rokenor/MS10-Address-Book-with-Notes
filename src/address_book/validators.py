from functools import wraps

from .classes import AddressBook, Record

def parse_input_validator(func):
    """Validator for parsing user input."""
    @wraps(func)
    def wrapper(user_input):
        if not user_input:
            return "Invalid input. Please enter a command."
        return func(user_input)
    return wrapper

def add_contact_validator(func):
    """Validator for adding a contact."""
    @wraps(func)
    def wrapper(args, contacts):
        if len(args) != 2:
            return "Invalid number of arguments. Usage: add <name> <phone>"
        name, phone = args
        if not name or not phone:
            return "Name and phone cannot be empty."
        return func(args, contacts)
    return wrapper

def add_address_validator(func):
    """Validator for adding an address to a contact."""
    @wraps(func)
    def wrapper(args, book: AddressBook):
        if len(args) < 2:
            return "Invalid number of arguments. Usage: add-address <name> <address>"
        name = args[0]
        if not name:
            return "Name cannot be empty."
        return func(args, book)
    return wrapper

def list_contacts_validator(func):
    """Validator for listing contacts."""
    @wraps(func)
    def wrapper(args, book: AddressBook):
        if not isinstance(book, AddressBook) or not book.data:
            return "No contacts found."
        return func(args, book)
    return wrapper

def find_contact_validator(func):
    """Validator for finding a contact."""
    @wraps(func)
    def wrapper(args, contacts):
        if len(args) != 1:
            return "Invalid number of arguments. Usage: find <name>"
        return func(args, contacts)
    return wrapper

def delete_contact_validator(func):
    """Validator for deleting a contact."""
    @wraps(func)
    def wrapper(args, contacts):
        if len(args) != 1:
            return "Invalid number of arguments. Usage: delete <name>"
        return func(args, contacts)
    return wrapper

def edit_address_validator(func):
    """Validator for editing a contact's address."""
    @wraps(func)
    def wrapper(args, book: AddressBook):
        if len(args) < 2:
            return "Invalid number of arguments. Usage: edit-address <name> <new_address>"
        name = args[0]
        if not name:
            return "Name cannot be empty."
        return func(args, book)
    return wrapper

def edit_phone_validator(func):
    """Validator for editing a contact's phone number."""
    @wraps(func)
    def wrapper(args, contacts):
        if len(args) != 3:
            return "Invalid number of arguments. Usage: edit-phone <name> <old_phone> <new_phone>"
        return func(args, contacts)
    return wrapper

def add_birthday_validator(func):
    """Validator for adding a birthday to a contact."""
    @wraps(func)
    def wrapper(args, book: AddressBook):
        if len(args) != 2:
            return "Invalid number of arguments. Usage: add_birthday <name> <birthday>"
        if not isinstance(book, AddressBook):
            return "Invalid address book instance."

        name, birthday = args
        if not name or not birthday:
            return "Name and birthday cannot be empty."

        r = Record('')
        try:
            r.add_birthday(birthday)
        except ValueError as e:
            return str(e)

        return func(args, book)
    return wrapper

def birthdays_validator(func):
    """Validator for listing upcoming birthdays."""
    @wraps(func)
    def wrapper(args, book: AddressBook):
        if not isinstance(book, AddressBook):
            return "Invalid address book instance."
        return func(args, book)
    return wrapper

def add_email_validator(func):
    """Validator for adding an email to a contact."""
    @wraps(func)
    def wrapper(args, book: AddressBook):
        if len(args) != 2:
            return "Invalid number of arguments. Usage: add-email <name> <email>"
        name, email = args
        if not name or not email:
            return "Name and email cannot be empty."
        return func(args, book)
    return wrapper

def edit_email_validator(func):
    """Validator for editing a contact's email."""
    @wraps(func)
    def wrapper(args, book: AddressBook):
        if len(args) != 2:
            return "Invalid number of arguments. Usage: edit-email <name> <new_email>"
        name, new_email = args
        if not name or not new_email:
            return "Name and new email cannot be empty."
        return func(args, book)
    return wrapper
