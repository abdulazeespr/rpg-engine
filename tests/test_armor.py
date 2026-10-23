import unittest

from domain.classes import Warrior
from domain.items import Armor


class ArmorTests(unittest.TestCase):
    def test_armor_increases_defense_and_reduces_incoming_damage(self):
        character = Warrior("Bram")
        character.take_damage(10)
        self.assertEqual(character.health, 110)

        message = Armor("Iron Armor", 5).apply(character)
        character.take_damage(10)

        self.assertEqual(character.defense, 5)
        self.assertEqual(character.health, 105)
        self.assertEqual(message, "Bram equips Iron Armor (+5 DEF)")

    def test_defense_cannot_reduce_damage_below_zero(self):
        character = Warrior("Bram")
        character.defense = 20
        character.take_damage(10)
        self.assertEqual(character.health, 120)

    def test_negative_defense_is_rejected(self):
        character = Warrior("Bram")
        with self.assertRaises(ValueError):
            character.defense = -1


if __name__ == "__main__":
    unittest.main()
