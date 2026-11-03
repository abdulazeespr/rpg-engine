from patterns.creational import CharacterFactory, EnemyBuilder
from domain.items import HealthPotion


# Using Factory
player = CharacterFactory.create("mage", "Sylla")


# Using Builder
boss = (EnemyBuilder("Dragon")
        .with_health(500)
        .with_attack(50)
        .with_loot(HealthPotion())
        .build())


print(f"Created {player.name} (HP: {player.health})")
print(f"Created {boss.name} (HP: {boss.health})")



    

   