class Warrior():
    '''
    Warrior is a base class for all warriors in the Battle.
    Use it to construct your own special Warrior Types
    '''
    
    #Power is the whole amount of energy that the warrior has.
    #It is distributed between
    #strength and health according to the hsfactor:
    # strength = __power * hsfactor
    # health   = __power * (1 - hsfactor)
    __power = 100
    __d = {

    }

    @classmethod
    def get_mess(cls, key):
        return cls.__d(key)
    
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
        #self.damage += self.prop * 1,1
        if self.is_dead():
            print("GOD: {} is dead. I'm sorry...".format(self.__name))
            return
        if damage > self.__strength:
            make_sound("It's too hard to me...")
            return
        self.make_sound("Taste my {}-power hit!".format(damage))
        enemy.defend(damage)
        self.__strength -= damage
        
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
    self.waithealth = self.__health * 1,1
    self.waitpower = self.__power * 1,1
    self.make_sound("I'm waiting! My strength is {} and health is {}".format(
        self.__strength,
        self.__health
    ))


class Experience ():

    def __init__(self, _experience = 0):
        self._experience = 0
        #self.victorycount = 10
        self._experience += self.victorycount

    @property
    def prop(self):
        return self._experience

class Orc (Warrior):
    def __init__(self, name):
        Warrior.__init__(self, name, hsfactor = 0.7)

    def attack(self, enemy):
        Warrior.attack(self, enemy, damage = 10)

    
    

    





    

