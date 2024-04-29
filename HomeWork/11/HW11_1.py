class Game:
    # Class attribute
    default_time_to_finish = 10.0  # In hours
    def __init__(self, name, time_to_finish=None):
        self._name = name
        self._time_to_finish = time_to_finish if time_to_finish is not None else self.default_time_to_finish

    # Getter and setter for instance attribute 'name'
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and setter for instance attribute 'time_to_finish'
    def get_time_to_finish(self):
        return self._time_to_finish

    def set_time_to_finish(self, time_to_finish):
        self._time_to_finish = time_to_finish

    # Getter and setter for class attribute 'default_time_to_finish'
    @classmethod
    def get_default_time_to_finish(cls):
        return cls.default_time_to_finish

    @classmethod
    def set_default_time_to_finish(cls, default_time_to_finish):
        cls.default_time_to_finish = default_time_to_finish


# Example usage
game1 = Game("Tetris")
game2 = Game("Mario", 15.5)

print(f"Game 1: {game1.get_name()}, Time to Finish: {game1.get_time_to_finish()} hours")
print(f"Game 2: {game2.get_name()}, Time to Finish: {game2.get_time_to_finish()} hours")

# Changing instance attributes using setters
game1.set_name("Pac-Man")
game1.set_time_to_finish(8.0)

print(f"Updated Game 1: {game1.get_name()}, Time to Finish: {game1.get_time_to_finish()} hours")

# Changing class attribute using setter
Game.set_default_time_to_finish(12.0)

print(f"Default Time to Finish: {Game.get_default_time_to_finish()} hours")
