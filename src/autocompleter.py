from prompt_toolkit.completion import Completer, Completion
from src.address_book.classes import AddressBook
from src.notes.handlers import note_book
import itertools

USER_SEARCHABLE_COMMANDS = [
    'add-address',
    'add-birthday',
    'add-email',
    'edit-address',
    'edit-birthday',
    'edit-phone',
    'edit-email',
    'search',
    'delete'
]

NOTES_SEARCHABLE_COMMANDS = [
    'note-edit',
    'note-tag',
    'note-delete',
]

NOTES_TAG_SEARCHABLE_COMMANDS = [
    'note-tag-search',
    'note-tag-sort',
]

def variants(variants: list, user_input: str):
    variants = [str(v) for v in variants]
    variants.sort()
    for v in variants:
        if str(v).startswith(user_input):
            yield Completion(v, start_position=-len(user_input))


class MultiStageCompleter(Completer):
    def __init__(self, commands, book: AddressBook):
        self.book = book
        self.commands = list(commands)

    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor.strip()
        words = text_before_cursor.split()

        # If currently typing a new word, count it in
        if document.text_before_cursor.endswith(" "):
            words.append("")

        index = len(words) - 1  # 0-based word index

        match index:
            case 0: yield from self.base_commands(words[0])
            case 1: yield from self.first_level_arg(words[0], words[1])
            case 2: yield from self.second_level_arg(words[0], words[1], words[2])
            case _: yield from []

    def base_commands(self, base_command):
        yield from variants(self.commands, base_command)

    def first_level_arg(self, base_command, first_arg):
        if base_command in USER_SEARCHABLE_COMMANDS:
            names = self.book.names()
        elif base_command in NOTES_SEARCHABLE_COMMANDS:
            names = note_book.data.keys()
        elif base_command in NOTES_TAG_SEARCHABLE_COMMANDS:
            names = [note.tags for note in note_book.data.values()]
            names = list(itertools.chain.from_iterable(names))
        else:
            names = []

        yield from variants(names, first_arg)

    def second_level_arg(self, base_command, first_arg, second_arg):
        if base_command == 'edit-phone':
            rec = self.book.find(first_arg)
            if not rec:
                yield from []
                return

            yield from variants(rec.phones, second_arg)
