class Warrior():
    '''
    Warrior is a base class for all wariors in the Battle.
    Use it to construct your own special Warrior Types
    '''
    
    #Power is the whole amount of energy that the warrior has.
    #It is distributed between
    #strength and healt h according to the hsfactor:
    # strength = __power * hsfactor
    # health   = __power * (1 - hsfactor)
    __power = 100
    __experience = 0
    
    @classmethod
    def get_power(cls):
        return cls.__power
    
    def __init__(self, name, hsfactor = 0.5):
        self.__name = name.upper()
        self.__health = round(Warrior.get_power() * hsfactor)
        self.__strength = round(Warrior.get_power() * (1 - hsfactor))
        power = self.__health + self.__strength # must be 1 after rounding
        if power > 1:
            self.__health - 1
        elif power < 1:
            self.__health + 1
        self.make_sound("I've born! My strenght is {} and health is {}".format(
            round(self.__strength),
            round(self.__health)
        ))
    
    def is_dead(self):
        return self.__health <= 0

    def make_sound(self, sound):
        print("{}: {}".format(self.__name, sound))   
    
    def attack(self, enemy, damage):
        if self.is_dead():
            print("GOD: {} is dead. I'm sorry...".format(self.__name))
            return

        if enemy.is_dead():
            self.make_sound("Oh snap! My enemy is already dead!")
            return

        if damage > self.__strength:
            self.make_sound("It's too hard to me...")
            return

        bonus_damage =  (damage * (0.1 * self.__experience))
        self.make_sound("Taste my {}-power hit!".format(damage + bonus_damage))
        enemy.defend(damage + bonus_damage)
        self.__strength -= damage
        if enemy.is_dead():
            self.increase_experience()
        
    def defend(self, damage):
        self.__health -= damage
        if self.is_dead():
            self.make_sound("...")
        else:
            self.make_sound("Oh!")

    def how_are_you(self):
        self.make_sound("I'm fine, tnx! My strength is {} and health is {}".format(
            self.__strength,
            self.__health
        ))
        
    def wait(self):
        self.__strength = self.__strength + (self.__strength * 0.1) 
        self.__health = self.__health + (self.__health * 0.1)
        self.make_sound("I feel myself better after waiting, tnx! My strength is {} and health is {}".format(
            self.__strength,
            self.__health
        ))

    def increase_experience(self):
        self.__experience += 1
        self.make_sound("Yahoooo my experience is increased! {}".format(self.__experience))

        
class Elf(Warrior):
    def __init__(self, name):
        super().__init__(name,  0.3)
    def __init__(self, sound):
        super().__init__(sound)
        self.make_sound("Yoloooo, I'm a super Elf!")

   
class Gnome(Warrior):
    def __init__(self, name):
        super().__init__(name,  0.5)
    def __init__(self, sound):
        super().__init__(sound)
        self.make_sound("Pffff, I'm a super Gnome!")

class Orc(Warrior):
    def __init__(self, name):
        super().__init__(name, 0.7)
    def __init__(self, sound):
        super().__init__(sound)
        self.make_sound("Arrrrrrr, I'm a super Orc!")


war1 = Elf("Princess Rose")
war2 = Gnome("King Wen")
war3 = Orc("King Gristle")

war1.attack(war2, 25)
war1.wait()
war1.wait()
war1.wait()
war1.attack(war2, 25)
war1.attack(war3, 5)


    





    

