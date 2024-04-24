class Game:
    # Class attribute (avg time to finish a game)
    default_time_to_finish = 10.0  # In hours

    def __init__(self, name, time_to_finish=None):
        self.name = name
        self.time_to_finish = time_to_finish if time_to_finish is not None else self.default_time_to_finish


game1 = Game("Tetris")
game2 = Game("Mario", 15.5)

print(f"Game 1: {game1.name}, Time to Finish: {game1.time_to_finish} hours")
print(f"Game 2: {game2.name}, Time to Finish: {game2.time_to_finish} hours")
