import src.address_book.handlers as handlers
import src.storage as storage
import src.address_book.validators as validators
from src.address_book.classes import AddressBook

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
from src.storage import load_notes

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
    "close": handlers.close,
    "exit": handlers.close,
    "hello": lambda args, book: "How can I help you?",
    "help": handlers.command_list,
    "add": handlers.add_contact,
    "add-address": handlers.add_address,
    "add-birthday": handlers.add_birthday,
    "add-email": handlers.add_email,
    "all": handlers.list_contacts,
    "search": handlers.find_contact,
    "change": handlers.change_contact,
    "show-birthday": handlers.show_birthday,
    "birthdays": handlers.birthdays,
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
    book = storage.load_data(default=AddressBook())
    print("Welcome to the assistant bot!")
    print(handlers.command_list())

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
        storage.save_data(book)

if __name__ == "__main__":
    main()