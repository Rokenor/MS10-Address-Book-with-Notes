import sys
from . import validators
from .classes import AddressBook, Record, Address, Email
from prettytable.colortable import ColorTable, Themes
from colorama import Fore, init
init(autoreset=True)

def close(args = None, book = None):
    """Exit the program"""
    print(Fore.GREEN + "Good bye!")
    sys.exit(0)

def command_list(args = None, book = None):
    """Prints a list of available commands."""
    print("\n")
    print(Fore.GREEN + "Available commands:")
    table = ColorTable(theme=Themes.OCEAN_DEEP)
    table.align = "l"
    table.field_names = [f"{Fore.YELLOW}Command", f"{Fore.YELLOW}Description"]
    table.add_rows(
        [[f"{Fore.GREEN}hello", f"{Fore.WHITE}Greet the user"],
        [f"{Fore.GREEN}close {Fore.WHITE}or {Fore.GREEN}exit", f"{Fore.WHITE}Exit the program"]],
        divider=True
    )
    table.add_rows(
        [[f"{Fore.GREEN}add {Fore.LIGHTGREEN_EX}<name> <phone>", f"{Fore.WHITE}Add a new contact"],
        [f"{Fore.GREEN}add-address {Fore.LIGHTGREEN_EX}<name> <address>", f"{Fore.WHITE}Add an address to a contact"],
        [f"{Fore.GREEN}add-birthday {Fore.LIGHTGREEN_EX}<name> <birthday>", f"{Fore.WHITE}Add a birthday to a contact"],
        [f"{Fore.GREEN}add-email {Fore.LIGHTGREEN_EX}<name> <email>", f"{Fore.WHITE}Add an email address to a contact"],
        [f"{Fore.GREEN}edit-address {Fore.LIGHTGREEN_EX}<name> <new_address>", f"{Fore.WHITE}Edit a contact's address"],
        [f"{Fore.GREEN}edit-phone {Fore.LIGHTGREEN_EX}<name> <old_phone> <new_phone>", f"{Fore.WHITE}Edit a contact's phone"],
        [f"{Fore.GREEN}edit-email {Fore.LIGHTGREEN_EX}<name> <new_email>", f"{Fore.WHITE}Edit a contact's email"],
        [f"{Fore.GREEN}edit-birthday {Fore.LIGHTGREEN_EX}<name> <new_birthday>", f"{Fore.WHITE}Edit a contact's birthday"],
        [f"{Fore.GREEN}birthdays {Fore.LIGHTGREEN_EX}<days>", f"{Fore.WHITE}List upcoming birthdays in the next <days> days"],
        [f"{Fore.GREEN}all", f"{Fore.WHITE}List all contacts"],
        [f"{Fore.GREEN}search {Fore.LIGHTGREEN_EX}<name>", f"{Fore.WHITE}Find a contact by name"],
        [f"{Fore.GREEN}delete {Fore.LIGHTGREEN_EX}<name>", f"{Fore.WHITE}Delete a contact"]],
        divider=True
    )
    table.add_rows(
        [[f"{Fore.GREEN}note {Fore.LIGHTGREEN_EX}<name> <text>", f"{Fore.WHITE}Add a new note"],
        [f"{Fore.GREEN}note-edit {Fore.LIGHTGREEN_EX}<name> <new_text>", f"{Fore.WHITE}Edit a note's text"],
        [f"{Fore.GREEN}note-search {Fore.LIGHTGREEN_EX}<text>", f"{Fore.WHITE}Search notes by content"],
        [f"{Fore.GREEN}note-tag {Fore.LIGHTGREEN_EX}<name> <tag>", f"{Fore.WHITE}Add a tag to a note"],
        [f"{Fore.GREEN}note-tag-search {Fore.LIGHTGREEN_EX}<tag>", f"{Fore.WHITE}Find notes with a specific tag"],
        [f"{Fore.GREEN}note-tag-sort {Fore.LIGHTGREEN_EX}<tag>", f"{Fore.WHITE}Sort notes by a tag"],
        [f"{Fore.GREEN}note-delete {Fore.LIGHTGREEN_EX}<name>", f"{Fore.WHITE}Delete a note"],
        [f"{Fore.GREEN}note-all", f"{Fore.WHITE}List all notes"]],
        divider=True
    )
    return table

@validators.add_contact_validator
def add_contact(args, book: AddressBook):
    """Adds a new contact to the address book."""
    name, phone = args
    record = book.find(name)
    message = Fore.GREEN + "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = Fore.GREEN + "Contact added."
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
        return Fore.RED + "Contact not found."
    record.add_address(address)
    return Fore.GREEN + "Address added."

@validators.list_contacts_validator
def list_contacts(_, book: AddressBook):
    """Returns a string containing all contacts in the address book."""
    print('\n')
    print(Fore.GREEN + "All contacts:")
    table = ColorTable(theme=Themes.OCEAN_DEEP)
    table.align = "r"
    table.field_names = [f"{Fore.YELLOW}Name", f"{Fore.YELLOW}Birthday", f"{Fore.YELLOW}Phones", f"{Fore.YELLOW}Address", f"{Fore.YELLOW}Email"]

    for rec in book.values():
        rec_name = rec.name
        rec_birthday = rec.birthday
        rec_phones = ', '.join(str(phone) for phone in rec.phones)
        rec_address = rec.address.value if isinstance(rec.address, Address) else 'None'
        rec_email = rec.email.value if isinstance(rec.email, Email) else 'None'

        table.add_row([rec_name, rec_birthday, rec_phones, rec_address, rec_email])
    return table

@validators.find_contact_validator
def find_contact(args, book: AddressBook):
    """Finds a contact by name and returns a string representation of the contact."""
    name = args[0]
    rec = book.find(name)

    if rec is None:
        return Fore.RED + "Contact not found."
    print('\n')
    print(Fore.GREEN + "Contact found:")
    table = ColorTable(theme=Themes.OCEAN_DEEP)
    table.align = "r"
    table.field_names = [f"{Fore.YELLOW}Name", f"{Fore.YELLOW}Birthday", f"{Fore.YELLOW}Phones", f"{Fore.YELLOW}Address", f"{Fore.YELLOW}Email"]
    table.add_row([rec.name, rec.birthday, ', '.join(str(phone) for phone in rec.phones), rec.address.value if isinstance(rec.address, Address) else 'None', rec.email.value if isinstance(rec.email, Email) else 'None'])
    return table

@validators.delete_contact_validator
def delete_contact(args, book: AddressBook):
    """Deletes a contact from the address book."""
    name = args[0]
    rec = book.find(name)
    if rec is None:
        return Fore.RED + "Contact not found."
    book.delete(rec.name.value)
    return Fore.GREEN + "Contact deleted."

@validators.edit_address_validator
def edit_address(args, book: AddressBook):
    """Edits a contact's address in the address book."""
    name = args[0]
    new_address = " ".join(args[1:])
    rec = book.find(name)
    if rec is None:
        return Fore.RED + "Contact not found."

    rec.edit_address(new_address)
    return Fore.GREEN + "Address updated."

@validators.edit_phone_validator
def edit_phone(args, book: AddressBook):
    """Edits a contact's phone number in the address book."""
    name, old_phone, new_phone = args
    rec = book.find(name)
    if rec is None:
        return Fore.RED + "Contact not found."

    rec.edit_phone(old_phone, new_phone)
    return Fore.GREEN + "Phone updated."

@validators.add_birthday_validator
def add_birthday(args, book: AddressBook):
    """Adds a birthday to a contact in the address book."""
    name, birthday = args
    record = book.find(name)
    if not record:
        return Fore.RED + "Contact not found."

    record.add_birthday(birthday)
    return Fore.GREEN + "Birthday added."

@validators.add_birthday_validator
def edit_birthday(args, book: AddressBook):
    """Edits a contact's birthday in the address book."""
    name, new_birthday = args
    rec = book.find(name)
    if rec is None:
        return Fore.RED + "Contact not found."

    rec.add_birthday(new_birthday)
    return Fore.GREEN + "Birthday updated."

@validators.birthdays_validator
def birthdays(args, book: AddressBook):
    """Returns a list of users who need to be greeted on the next week"""
    upcoming_days = int(args[0])
    birthdays_list = book.get_upcoming_birthdays(upcoming_days)
    if not birthdays_list:
        return Fore.RED + "No upcoming birthdays."
    print('\n')
    print(Fore.GREEN + "Upcoming birthdays:")
    table = ColorTable(theme=Themes.OCEAN_DEEP)
    table.align = "r"
    table.field_names = [f"{Fore.YELLOW}Name", f"{Fore.YELLOW}Birthday"]
    table.add_rows(
        [[record.name, record.birthday] for record in birthdays_list],
        divider=True
    )
    return table

@validators.add_email_validator
def add_email(args, book: AddressBook):
    """Adds an email address to a contact in the address book."""
    name, email = args
    record = book.find(name)
    if record is None:
        return Fore.RED + "Contact not found."
    record.add_email(email)
    return Fore.GREEN + "Email added."

@validators.edit_email_validator
def edit_email(args, book: AddressBook):
    """Edits a contact's email address in the address book."""
    name, new_email = args
    rec = book.find(name)
    if rec is None:
        return Fore.RED + "Contact not found."

    rec.add_email(new_email)
    return Fore.GREEN + "Email updated."
