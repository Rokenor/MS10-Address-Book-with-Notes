import src.address_book.validators as validators
from src.address_book.classes import AddressBook

from src.address_book.handlers import (
    close,
    command_list,
    add_contact,
    add_address,
    add_birthday,
    add_email,
    birthdays,
    list_contacts,
    find_contact,
    delete_contact,
    edit_address,
    edit_phone,
    edit_email,
    edit_birthday
)

from src.notes.handlers import (
    note_book,
    note_add_command,
    note_edit_command,
    note_search_command,
    note_tag_command,
    note_tag_search_command,
    note_tag_sort_command,
    note_delete_command,
    note_all_command
)

from src.storage import (load_data, save_data, load_notes)

loaded_notes = load_notes(default=note_book)
if loaded_notes:
    note_book.data = loaded_notes.data

@validators.parse_input_validator
def parse_input(user_input):
    """Parses user input into a command and arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

commands = {
    "close": close,
    "exit": close,
    "hello": lambda args, book: "How can I help you?",
    "help": command_list,
    "add": add_contact,
    "add-address": add_address,
    "add-birthday": add_birthday,
    "add-email": add_email,
    "birthdays": birthdays,
    "all": list_contacts,
    "search": find_contact,
    "delete": delete_contact,
    "edit-address": edit_address,
    "edit-phone": edit_phone,
    "edit-email": edit_email,
    "edit-birthday": edit_birthday,
    "note": note_add_command,
    "note-edit": note_edit_command,
    "note-search": note_search_command,
    "note-tag": note_tag_command,
    "note-tag-search": note_tag_search_command,
    "note-tag-sort": note_tag_sort_command,
    "note-all": note_all_command,
    "note-delete": note_delete_command
}

def main():
    """Main function."""
    book = load_data(default=AddressBook())
    print("Welcome to the assistant bot!")
    print(command_list())

    try:
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in commands:
                try:
                    result = commands[command](args, book)
                    if result is not None:
                        print(result)
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Invalid command. Please try again.")
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")
    finally:
        save_data(book)

if __name__ == "__main__":
    main()
