from .classes import Note, NoteBook
from src.storage import save_notes

note_book = NoteBook()

def note_add(name: str, text: str) -> str:
    if name in note_book.data:
        return f"Нотатка з назвою '{name}' вже існує."

    note = Note(name, text)
    note_book.add_note(note)
    save_notes(note_book)  # ЗБЕРЕЖЕННЯ
    return f"Нотатку '{name}' додано успішно."

def note_edit(name: str, new_text: str) -> str:
    note = note_book.data.get(name)
    if not note:
        return f"Нотатку з назвою '{name}' не знайдено."

    note.edit_text(new_text)
    save_notes(note_book)  # ЗБЕРЕЖЕННЯ
    return f"Текст нотатки '{name}' успішно змінено."

def note_search(text: str) -> str:
    results = note_book.find_by_text(text)
    if not results:
        return f"Нотаток з текстом '{text}' не знайдено."

    output = "Знайдені нотатки:\n"
    output += "\n\n".join(str(note) for note in results)
    return output

def note_tag(name: str, tag: str) -> str:
    note = note_book.data.get(name)
    if not note:
        return f"Нотатку з назвою '{name}' не знайдено."

    note.add_tag(tag)
    save_notes(note_book)  # ЗБЕРЕЖЕННЯ
    return f"Тег '{tag}' додано до нотатки '{name}'."

def note_tag_search(tag: str) -> str:
    results = note_book.find_by_tag(tag)
    if not results:
        return f"Нотаток з тегом '{tag}' не знайдено."

    output = f"Нотатки з тегом '{tag}':\n"
    output += "\n\n".join(str(note) for note in results)
    return output

def note_tag_sort(tag: str) -> str:
    sorted_notes = note_book.sort_by_tag(tag)
    if not sorted_notes:
        return f"Нотаток з тегом '{tag}' не знайдено."

    output = f"Нотатки з тегом '{tag}' (відсортовано за назвою):\n"
    output += "\n\n".join(str(note) for note in sorted_notes)
    return output

def note_all() -> str:
    if not note_book.data:
        return "Нотаток поки немає."

    output = "Усі нотатки:\n"
    output += "\n\n".join(str(note) for note in note_book.data.values())
    return output

def note_delete(name: str) -> str:
    if name not in note_book.data:
        return f"Нотатку з назвою '{name}' не знайдено."

    note_book.delete_note(name)
    save_notes(note_book)  # ЗБЕРЕЖЕННЯ
    return f"Нотатку '{name}' успішно видалено."



def note_add_command(args: list[str], book=None) -> str:
    if len(args) < 2:
        return "Команда має містити назву та текст нотатки."
    name = args[0]
    text = " ".join(args[1:])
    return note_add(name, text)

def note_edit_command(args: list[str], book=None) -> str:
    if len(args) < 2:
        return "Команда має містити назву нотатки та новий текст."
    name = args[0]
    new_text = " ".join(args[1:])
    return note_edit(name, new_text)

def note_search_command(args: list[str], book=None) -> str:
    if not args:
        return "Вкажіть текст для пошуку."
    return note_search(" ".join(args))

def note_tag_command(args: list[str], book=None) -> str:
    if len(args) < 2:
        return "Вкажіть назву нотатки та тег."
    return note_tag(args[0], args[1])

def note_tag_search_command(args: list[str], book=None) -> str:
    if not args:
        return "Вкажіть тег для пошуку."
    return note_tag_search(args[0])

def note_tag_sort_command(args: list[str], book=None) -> str:
    if not args:
        return "Вкажіть тег для сортування."
    return note_tag_sort(args[0])

def note_all_command(args: list[str], book=None) -> str:
    return note_all()

def note_delete_command(args: list[str], book=None) -> str:
    if not args:
        return "Вкажіть назву нотатки для видалення."
    return note_delete(args[0])
