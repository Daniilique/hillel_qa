class Game:
    def __init__(self, name, time_to_finish=None):
        self._name = name
        self._time_to_finish = time_to_finish

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_time_to_finish(self):
        return self._time_to_finish

    def set_time_to_finish(self, time_to_finish):
        self._time_to_finish = time_to_finish


class ExtendedGame(Game):
    def __init__(self, name, time_to_finish=None, multiplayer=False):
        super().__init__(name, time_to_finish)
        self.multiplayer = multiplayer

    def is_multiplayer(self):
        return self.multiplayer

    # New method added to the child class
    def time_per_player(self, num_players):
        if self.multiplayer:
            return self._time_to_finish / num_players
        else:
            return self._time_to_finish


# Example usage
extended_game = ExtendedGame("Call of Duty", 20.0, True)
print(f"Extended Game: {extended_game.get_name()}, Time to Finish: {extended_game.get_time_to_finish()} hours, Multiplayer: {extended_game.is_multiplayer()}")

# Using the new method
print(f"Time per player: {extended_game.time_per_player(4)} hours")
