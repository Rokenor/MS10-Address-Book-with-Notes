from .classes import Note, NoteBook
from src.storage import save_notes
from prettytable.colortable import ColorTable, Themes
from colorama import Fore, init
init(autoreset=True)

note_book = NoteBook()

def note_add(name: str, text: str) -> str:
    """Adds a new note to the note book."""
    if name in note_book.data:
        return Fore.RED + f"Note with name '{name}' already exists."

    note = Note(name, text)
    note_book.add_note(note)
    save_notes(note_book)  # SAVE
    return Fore.GREEN + f"Note '{name}' added successfully."

def note_edit(name: str, new_text: str) -> str:
    """Edits a note in the note book."""
    note = note_book.data.get(name)
    if not note:
        return Fore.RED + f"Note with name '{name}' not found."

    note.edit_text(new_text)
    save_notes(note_book)  # SAVE
    return Fore.GREEN + f"Text of note '{name}' successfully changed."

def note_search(text: str) -> str:
    """Returns a list of notes containing the given text."""
    results = note_book.find_by_text(text)
    if not results:
        return Fore.RED + f"Notes with text '{text}' not found."

    print('\n')
    print(Fore.GREEN + "Search results:")
    table = ColorTable(theme=Themes.OCEAN_DEEP)
    table.field_names = [f"{Fore.YELLOW}Name", f"{Fore.YELLOW}Text", f"{Fore.YELLOW}Tags"]
    table.align[f"{Fore.YELLOW}Name"] = "l"
    table.align[f"{Fore.YELLOW}Text"] = "l"
    table.align[f"{Fore.YELLOW}Tags"] = "r"
    
    for note in results:
        table.add_row([note.name, Fore.WHITE + note.text, ', '.join(note.tags)])
        table.add_divider()
    
    return table

def note_tag(name: str, tag: str) -> str:
    """Adds a tag to a note."""
    note = note_book.data.get(name)
    if not note:
        return Fore.RED + f"Note with name '{name}' not found."

    note.add_tag(tag)
    save_notes(note_book)  # SAVE
    return Fore.GREEN + f"Tag '{tag}' added to note '{name}'."

def note_tag_search(tag: str) -> str:
    """Returns a list of notes containing the given tag."""
    results = note_book.find_by_tag(tag)
    if not results:
        return Fore.RED + f"No notes found with tag '{tag}'."

    print('\n')
    print(Fore.GREEN + "Search by tag results:")
    table = ColorTable(theme=Themes.OCEAN_DEEP)
    table.field_names = [f"{Fore.YELLOW}Name", f"{Fore.YELLOW}Text", f"{Fore.YELLOW}Tags"]
    table.align[f"{Fore.YELLOW}Name"] = "l"
    table.align[f"{Fore.YELLOW}Text"] = "l"
    table.align[f"{Fore.YELLOW}Tags"] = "r"
    
    for note in results:
        table.add_row([note.name, Fore.WHITE + note.text, ', '.join(note.tags)])
        table.add_divider()
    
    return table

def note_tag_sort(tag: str) -> str:
    """Returns a list of notes sorted by the given tag."""
    sorted_notes = note_book.sort_by_tag(tag)
    if not sorted_notes:
        return Fore.RED + f"No notes found with tag '{tag}'."

    print('\n')
    print(Fore.GREEN + "Sorted notes by tag results:")
    table = ColorTable(theme=Themes.OCEAN_DEEP)
    table.field_names = [f"{Fore.YELLOW}Name", f"{Fore.YELLOW}Text", f"{Fore.YELLOW}Tags"]
    table.align[f"{Fore.YELLOW}Name"] = "l"
    table.align[f"{Fore.YELLOW}Text"] = "l"
    table.align[f"{Fore.YELLOW}Tags"] = "r"
    
    for note in sorted_notes:
        table.add_row([note.name, Fore.WHITE + note.text, ', '.join(note.tags)])
        table.add_divider()
    
    return table

def note_all() -> str:
    """Returns a table of all notes."""
    if not note_book.data:
        return Fore.RED + "No notes found."

    print('\n')
    print(Fore.GREEN + "All notes:")
    table = ColorTable(theme=Themes.OCEAN_DEEP)
    table.field_names = [f"{Fore.YELLOW}Name", f"{Fore.YELLOW}Text", f"{Fore.YELLOW}Tags"]
    table.align[f"{Fore.YELLOW}Name"] = "l"
    table.align[f"{Fore.YELLOW}Text"] = "l"
    table.align[f"{Fore.YELLOW}Tags"] = "r"
    
    for note in note_book.data.values():
        table.add_row([note.name, Fore.WHITE + note.text, ', '.join(note.tags)])
        table.add_divider()
    
    return table

def note_delete(name: str) -> str:
    """Deletes a note from the note book."""
    if name not in note_book.data:
        return Fore.RED + f"No note found with name '{name}'."

    note_book.delete_note(name)
    save_notes(note_book)  # SAVE
    return Fore.GREEN + f"Note '{name}' deleted successfully."

def note_add_command(args: list[str], book=None) -> str:
    """Adds a new note to the note book."""
    if len(args) < 2:
        return Fore.RED + "Enter note name and text."
    name = args[0]
    text = " ".join(args[1:])
    return note_add(name, text)

def note_edit_command(args: list[str], book=None) -> str:
    """Edits a note in the note book."""
    if len(args) < 2:
        return Fore.RED + "Enter note name and new text."
    name = args[0]
    new_text = " ".join(args[1:])
    return note_edit(name, new_text)

def note_search_command(args: list[str], book=None) -> str:
    """Returns a list of notes containing the given text."""
    if not args:
        return Fore.RED + "Enter text to search for."
    return note_search(" ".join(args))

def note_tag_command(args: list[str], book=None) -> str:
    """Adds a tag to a note."""
    if len(args) < 2:
        return Fore.RED + "Enter note name and tag."
    return note_tag(args[0], args[1])

def note_tag_search_command(args: list[str], book=None) -> str:
    """Returns a list of notes containing the given tag."""
    if not args:
        return Fore.RED + "Enter tag to search for."
    return note_tag_search(args[0])

def note_tag_sort_command(args: list[str], book=None) -> str:
    """Returns a list of notes sorted by the given tag."""
    if not args:
        return Fore.RED + "Enter tag to sort by."
    return note_tag_sort(args[0])

def note_all_command(args: list[str], book=None) -> str:
    """Returns a table of all notes."""
    return note_all()

def note_delete_command(args: list[str], book=None) -> str:
    """Deletes a note from the note book."""
    if not args:
        return Fore.RED + "Enter note name to delete."
    return note_delete(args[0])
