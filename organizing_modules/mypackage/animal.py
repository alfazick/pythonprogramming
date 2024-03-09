class Animal:
    def __init__(self,sound) -> None:
        self.sound = sound 

    def say(self):
        print(f"{self.sound} {self.sound} {self.sound}")

    