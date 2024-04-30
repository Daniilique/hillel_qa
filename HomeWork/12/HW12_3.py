class MyContextManager:
    def __init__(self, game):
        self.game = game

    def __enter__(self):
        print("Starting game session:", self.game)
        return self.game

    def __exit__(self, exc_type, exc_value, traceback):
        print("Ending game session:", self.game)

with MyContextManager('Super Mario'):
    print("Playing Super Mario...")

print("Outside of the game session.")
