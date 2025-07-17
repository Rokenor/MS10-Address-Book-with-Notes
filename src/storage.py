import pickle
import os

def save_data(book, filename="storage/addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="storage/addressbook.pkl", default=None):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return default

NOTES_FILE = os.path.join(os.path.expanduser("~"), ".my_assistant_data", "notes.pkl")

def save_notes(notes, filename=NOTES_FILE):
    """Зберігає NoteBook у файл у домашній папці користувача."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wb") as f:
        pickle.dump(notes, f)

def load_notes(filename=NOTES_FILE, default=None):
    """Завантажує NoteBook із файлу або повертає значення default."""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return default
