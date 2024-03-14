# storage.py 
def save_notes(notes):
    with open("notes.txt", "w") as f:
        for note in notes:
            f.write(f"{note}\n")


def load_notes():
    try:
        with open("notes.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []
    

