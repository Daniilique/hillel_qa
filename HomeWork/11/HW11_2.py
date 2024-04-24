class Game:
    pass

class ExtendedGame(Game):
    def __init__(self, name, time_to_finish=None, multiplayer=False):
        super().__init__(name, time_to_finish)
        self.multiplayer = multiplayer

    def is_multiplayer(self):
        return self.multiplayer

extended_game = ExtendedGame("Call of Duty", 20.0, True)
print(f"Extended Game: {extended_game.name}, Time to Finish: {extended_game.time_to_finish} hours, Multiplayer: {extended_game.is_multiplayer()}")
