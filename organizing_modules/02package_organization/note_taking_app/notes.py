# notes.py

from .storage import load_notes, save_notes

def add_note(note):
    notes = load_notes()
    notes.append(note)
    save_notes(notes)

def get_notes():
    return load_notes()


def update_note(index,new_note):
    notes = load_notes()
    if 0 <= index < len(notes):
        notes[index] = new_note
        save_notes(notes)

def delete_note(index):
    notes = load_notes()
    if 0 <=index < len(notes):
        notes.pop(index)
        save_notes(notes)

