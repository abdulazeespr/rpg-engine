from patterns.singleton import GameManager


# Get the manager and set some state
# manager1 = GameManager()
# manager1.difficulty = "hard"


# # Somewhere else in the code, we try to create a new manager
# manager2 = GameManager()


# print(f"Manager 2 difficulty: {manager2.difficulty}") 
# # Outputs "hard" because manager1 and manager2 are the exact same object!


# print(f"Are they the same object? {manager1 is manager2}")

def get_combat_manager():
    return GameManager()


def get_menu_manager():
    return GameManager()


combat_manager = get_combat_manager()
menu_manager = get_menu_manager()

print(combat_manager is menu_manager)
print(id(combat_manager), id(menu_manager))