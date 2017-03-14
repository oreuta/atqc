class Warrior():

    def __init__(self, name, strength, health):
        self.__name = name
        self.__strength = strength
        self.__health = health
        print("I've born")

    def attack(self, enemy, damage):
        # damage <= __strength
        enemy.defend(damage)
        self.__strength -= damage)

    def defend(self, damage):
        self.__health -= damage
        # dead ?


# Battle
w1 = Warrior(...)
w2 = Warrior(...)
w1.attack(w2)
if w2.isAlive:
    ...
w2.attack(w1)
if w1.isAlive:
    ...
    




    





    

