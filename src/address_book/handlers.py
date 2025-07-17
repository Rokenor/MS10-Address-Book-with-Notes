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
        "- birthdays <days>: List upcoming birthdays in the next <days> days\n"
        "- all: List all contacts\n"
        "- search <name>: Find a contact by name\n"
        "- delete <name>: Delete a contact\n"
        "- edit-address <name> <new_address>: Edit a contact's address\n"
        "- edit-phone <name> <old_phone> <new_phone>: Edit a contact's phone\n"
        "- edit-email <name> <new_email>: Edit a contact's email\n"
        "- edit-birthday <name> <new_birthday>: Edit a contact's birthday\n"
        "- show-birthday <name>: Show a contact's birthday\n"
        "- note <name> <text>: Add a new note\n"
        "- note-edit <name> <new_text>: Edit a note's text\n"
        "- note-search <text>: Search notes by content\n"
        "- note-tag <name> <tag>: Add a tag to a note\n"
        "- note-tag-search <tag>: Find notes with a specific tag\n"
        "- note-tag-sort <tag>: Sort notes by a tag\n"
        "- note-delete <name>: Delete a note\n"
        "- note-all: List all notes\n"
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

@validators.add_address_validator
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

@validators.delete_contact_validator
def delete_contact(args, book: AddressBook):
    """Deletes a contact from the address book."""
    name = args[0]
    rec = book.find(name)
    if rec is None:
        return "Contact not found."
    book.delete(rec.name.value)
    return "Contact deleted."

@validators.edit_address_validator
def edit_address(args, book: AddressBook):
    """Edits a contact's address in the address book."""
    name = args[0]
    new_address = " ".join(args[1:])
    rec = book.find(name)
    if rec is None:
        return "Contact not found."

    rec.edit_address(new_address)
    return "Address updated."

@validators.edit_phone_validator
def edit_phone(args, book: AddressBook):
    """Edits a contact's phone number in the address book."""
    name, old_phone, new_phone = args
    rec = book.find(name)
    if rec is None:
        return "Contact not found."

    rec.edit_phone(old_phone, new_phone)
    return "Phone updated."

@validators.add_birthday_validator
def add_birthday(args, book: AddressBook):
    """Adds a birthday to a contact in the address book."""
    name, birthday = args
    record = book.find(name)
    if not record:
        return "Contact not found."

    record.add_birthday(birthday)
    return "Birthday added."

@validators.add_birthday_validator
def edit_birthday(args, book: AddressBook):
    """Edits a contact's birthday in the address book."""
    name, new_birthday = args
    rec = book.find(name)
    if rec is None:
        return "Contact not found."

    rec.add_birthday(new_birthday)
    return "Birthday updated."

@validators.birthdays_validator
def birthdays(args, book: AddressBook):
    """Returns a list of users who need to be greeted on the next week"""
    upcoming_days = int(args[0])
    birthdays_list = book.get_upcoming_birthdays(upcoming_days)
    if not birthdays_list:
        return "No upcoming birthdays."
    return "\n".join(f"{record.name}: {record.birthday}" for record in birthdays_list)

@validators.add_email_validator
def add_email(args, book: AddressBook):
    """Adds an email address to a contact in the address book."""
    name, email = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.add_email(email)
    return "Email added."

@validators.edit_email_validator
def edit_email(args, book: AddressBook):
    """Edits a contact's email address in the address book."""
    name, new_email = args
    rec = book.find(name)
    if rec is None:
        return "Contact not found."

    rec.add_email(new_email)
    return "Email updated."
