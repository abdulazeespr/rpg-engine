aim to learn oops along with building project

some thoughts Note :

Class - it is blueprint .it have attributes and methods .use class we can create as many object we can
object - object is instance of class which same attributes and method which on same class . with it own values and memory 

if car as a class which atrributes like brand,colour,engine..etc and methods like driver,horn,break,light..etc
based blueprint or class we can create instance or object from that like bmw,range rover,defenderfortuner..etc


current we can access some variable direct accesss to change without vaildation or restrictions . when we decided encapsulate varliable private,procteted .so that i can access on class not outside the class .when you try access .get error like . you reference class structure domain/character.py
code :-
 goblin.health -= 50
    print(goblin.describe())
error:- 
Traceback (most recent call last):
  File "/home/support/rpg-engine/play.py", line 27, in <module>
    goblin.health -= 50
    ^^^^^^^^^^^^^
AttributeError: property 'health' of 'Character' object has no setter

so you only read the variable and can't update 

 Inheritance 
 -------------

 when create class in future we use some prorties and functions from class and also some special or extra for spefic . you can use  Inheritance class . which means rather copy class you use like relationship child-parent you can get all from parent if need you can update or overide functions and create new . 

 polymoriphism
 ------------
use to in same class have same function with diferent paramas for different behaviours . it can use overide the superclass .


 abstract 
 ------------
 why need abstract ? when create subclass but forget or you not implemenate function which is improtant when inheritance from super class . without abstract contract it let you create class . but with abstract contract it give power and strict rule you need implemente function otherwise it not create and give error like this
 Traceback (most recent call last):
  File "/home/support/rpg-engine/play.py", line 6, in <module>
    test_character = Character("Test", 10, 1)
TypeError: Can't instantiate abstract class Character without an implementation for abstract method 'special_ability'

composition
-----------
inheritance it follow 'is a ' relationship but composition follow 'has a' relationship . both are used to create class relationship . in compostion means when class use another class or another another method inside .

Custom Error 
-------------
rather get some not vaild interger ,number something error can more readable and more use debug

SOLID
current we use S — Single Responsibility Principle
a class should have one reason to change. which item split into usable,equippable

Factory & Builder
----------------
factory means function or class can deciding which class create to reduce under classes .which one class for create all character rather indiviual class for each Character

builder is class which if class have many object are optional the rather create class with constructor with parameter .build class incremently

Why not make every class a singleton?
-------------------------------------
A singleton allows only one shared instance, but a game needs many independent objects of classes like `Character`, each with its own name, health, and abilities. If `Character` were a singleton, creating another character could return the same object and overwrite or share the first character's state. This would make it difficult to represent a party of characters and would tightly couple parts of the game that should be independent.