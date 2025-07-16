import src.address_book.handlers as handlers
import src.storage as storage
import src.address_book.validators as validators
from src.address_book.classes import AddressBook


@validators.parse_input_validator
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

commands = {
    "close": handlers.close,
    "exit": handlers.close,
    "hello": lambda args, book: "How can I help you?",
    "help": handlers.help,
    "add": handlers.add_contact,
    "change": handlers.change_contact,
    "phone": handlers.find_contact,
    "all": handlers.list_contacts,
    "add-birthday": handlers.add_birthday,
    "show-birthday": handlers.show_birthday,
    "birthdays": handlers.birthdays
}

def main():
    book = storage.load_data(default=AddressBook())
    print("Welcome to the assistant bot!")
    print(handlers.help())

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