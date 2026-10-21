from domain.character import Character
from domain.classes import Warrior, Mage,Cleric,Rogue
from domain.battle import run_special_round,total_party_damage

if __name__ == "__main__":
    test_character = Character("Test", 10, 1)
    party = [Warrior("Bram"),Mage("Sylla"),Rogue("kade")]
    dummy = Warrior("Training Dummy")

    for member in party:
        #same function call,but completely different behaviour each time!

        run_special_round(member,dummy)
        print(f"Dummy HP:{dummy.health} \n")
    cleric = Cleric("Asha")
    target = Character("Dummy", health=100, attack_power=0)

    damage = total_party_damage([cleric], target)

    print(damage)        # 5
    print(target.health) # 95




    

   