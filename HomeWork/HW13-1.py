def videogame_singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@videogame_singleton
class GameManager:
    def __init__(self, game):
        self.game = game

manager1 = GameManager("Super Mario")
manager2 = GameManager("Legend of Zelda")

print(manager1.game)  # Output: Super Mario
print(manager2.game)  # Output: Super Mario (same instance as manager1)
print(manager1 is manager2)  # Output: True (both variables refer to the same instance)
