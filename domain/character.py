from abc import ABC, abstractmethod
from domain.inventory import Inventory

class Character(ABC):
    def __init__(self, name: str, health: int, attack_power: int, defense: int = 0):
        self.name = name
        self._health = health # protected: "internal use, but not enforced"
        self.inventory = Inventory()
        self.defense = defense
        self.__max_health = health # private: name-mangled, harder to touch by accident
        self.attack_power = attack_power

    @property
    def health(self)-> int:
        return self._health

    @property
    def is_alive(self) -> bool:
        return self._health > 0 

    @property
    def defense(self) -> int:
        return self._defense

    @defense.setter
    def defense(self, value: int) -> None:
        if value < 0:
            raise ValueError("Defense cannot be negative")
        self._defense = value

    def take_damage(self,amount:int) -> None:
        if amount < 0 :
            raise ValueError("Damage Cannot be Negative")
        self._health = max(0, self._health - max(0, amount - self.defense))
 

    def describe(self) -> str:
        return f"{self.name} has {self.health} HP and {self.attack_power} ATK"


    def attack(self, target: "Character") -> None:
        if not self.is_alive:
            return
        target.take_damage(self.attack_power)
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

    def heal(self,amount:int) -> None:
        if amount < 0 :
                raise ValueError("Heal Cannot be Negative")
        
        self._health = min(self.__max_health,self._health + amount)
        print(f"{self.name} heals for {amount} HP!")    

    @abstractmethod
    def special_ability(self,target: "Character") -> None:
           """Every concrete Character MUST define its own special move."""
           raise NotImplementedError