from domain.character import Character


def run_special_round(attacker:Character,defender:Character)->None:
    """Works for ANY Character subclass -this is polymorphism on action """
    attacker.special_ability(defender)

def total_party_damage(party, target):
    starting_health = target.health

    for character in party:
        character.attack(target)

    return starting_health - target.health    