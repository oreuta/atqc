'''Warrior'''

class Warrior():
    '''
    Warrior is a base class for all wariors in the Battle.
    Use it to construct your own special Warrior Types
    '''
    
    #Power is the whole amount of energy that the warrior has.
    #It is distributed between
    #strength and health according to the hsfactor:
    # strength = __power * hsfactor
    # health   = __power * (1 - hsfactor)
    __power = 100

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
        self.__strength = round(self.__strength * 1.1)
        self.__health = round(self.__health * 1.1)
        self.make_sound("Master, I feel good! My strength is {} and health is {}".format(
            self.__strength,
            self.__health
        ))
  
'''Exp'''

class Exp():
    def __init__(self):
       self.__exp = 0  
    def get__exp(self):
       return self.__exp
    def set__exp(self):
       if self.__win == True:
           self.__exp = self._exp + 1
       else:
           self.__exp = self.__exp


'''Elf'''

class Elf(Warrior):
    def __init__(self, name):
       Warrior.__init__(self, name, hsfactor = 0.3)


'''Gnome'''

class Gnome(Warrior):
    def __init__(self, name):
       Warrior.__init__(self, name, hsfactor = 0.4)


'''Orc'''

class Orc(Warrior):
    def __init__(self, name):
       Warrior.__init__(self, name, hsfactor = 0.7)
    
    def attack(self, enemy, damage = 10):
        pass
        
        '''if self.is_dead():
            print("GOD: {} is dead. I'm sorry...".format(self.__name))
            return
        if damage > self.__strength:
            make_sound("It's too hard to me...")
            return
        self.make_sound("Taste my {}-power hit!".format(damage))
        enemy.defend(damage)
        self.__strength -= damage'''


'''Test'''

def test():
    return(
    e == Elf('Elf'),
    o == Orc('Orc'))

 

    

