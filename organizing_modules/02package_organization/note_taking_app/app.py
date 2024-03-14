# app.py

from .notes import add_note, get_notes, update_note, delete_note

def main():
    while True:
        action = input("Choose an action: [A]dd, [V]iew, [U]pdate, [D]elete, [Q]uit: ").upper()

        match action:
            case "A":
                note = input("Enter the note: ")
                add_note(note)
            case "V":
                notes = get_notes()
                for index, note in enumerate(notes):
                    print(f"{index}: {note}")
            case "U":
                index = int(input("Enter the note index to update: "))
                new_note = input("Enter the new note: ")
                update_note(index, new_note)
            case "D":
                index = int(input("Enter the note index to delete: "))
                delete_note(index)
            case "Q":
                break

if __name__ == "__main__":
    main()


# to execute python -m note_taking_app.app
