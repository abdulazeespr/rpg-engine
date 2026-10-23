from domain.classes import Warrior, Mage, Cleric, Rogue
from domain.battle import run_special_round, total_party_damage
from domain.items import HealthPotion, Weapon

if __name__ == "__main__":
    party = [Warrior("Bram"),Mage("Sylla"),Rogue("kade")]
    dummy = Warrior("Training Dummy")

    character = party[0]
    character.take_damage(30)
    character.inventory.add(HealthPotion())
    character.inventory.add(HealthPotion())
    character.inventory.add(Weapon("Iron Sword", 5))
    print(f"{character.name}'s inventory: {character.inventory.list_items()}")
    for _ in range(3):
        print(character.inventory.use(0, character))

    for member in party:
        #same function call,but completely different behaviour each time!

        run_special_round(member,dummy)
        print(f"Dummy HP:{dummy.health} \n")
    cleric = Cleric("Asha")
    target = Warrior("Dummy")
    target.take_damage(20)

    damage = total_party_damage([cleric], target)

    print(damage)        # 5
    print(target.health)




    

   