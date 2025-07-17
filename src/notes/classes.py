from collections import UserDict

class Note:
    def __init__(self, name: str, text: str):
        self.name = name
        self.text = text
        self.tags = []

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def edit_text(self, new_text: str):
        self.text = new_text

    def __str__(self):
        return f"Назва: {self.name}\nТекст: {self.text}\nТеги: {', '.join(self.tags)}"

class NoteBook(UserDict):
    def add_note(self, note: Note):
        self.data[note.name] = note

    def delete_note(self, name: str):
        if name in self.data:
            del self.data[name]

    def find_by_text(self, text: str):
        return [note for note in self.data.values() if text.lower() in note.text.lower()]

    def find_by_tag(self, tag: str):
        return [note for note in self.data.values() if tag in note.tags]

    def sort_by_tag(self, tag: str):
        return sorted(self.find_by_tag(tag), key=lambda n: n.name.lower())