from domain.character import Character



if __name__ == "__main__":
    hero = Character("Aria", 100, 15)
    goblin = Character("Goblin", 30, 5)
    kim = Character("Kim",200,25)
    raju = Character("Raju",50,1)

    print(hero.describe())
    print(goblin.describe())
    print(kim.describe())
    print(raju.describe())


    hero.take_damage(150)
    # hero.take_damage(-150)
    hero.attack(goblin)
    print(goblin.describe())
    kim.attack(raju)
    print(raju.describe())
    raju.heal(10)
    goblin.attack(kim)
    print(kim.describe())
    kim.heal(250)
    kim.attack(hero)
    print(hero.describe())
    hero.heal(-50)
    print(goblin.health )
    print(raju.describe())
    raju.heal(10)
    goblin.attack(kim)
    print(kim.describe())
    # goblin.health -= 50
  
    print(goblin.describe())






    

   