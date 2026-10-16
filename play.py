from domain.character import Character
from domain.classes import Warrior, Mage,Cleric


if __name__ == "__main__":
  warrior = Warrior("Bram")
  mage = Mage("Sylla")
  cleric = Cleric("bob") 

  warrior.attack(mage)
  mage.attack(warrior)           
  # Reusing parent Character methodmage.special_ability(warrior)   # Using specialized Mage method
  print(f"Bram HP: {warrior.health}, Sylla HP: {mage.health}")
  print(warrior.describe())
  cleric.special_ability(warrior)
  print(warrior.describe())







    

   