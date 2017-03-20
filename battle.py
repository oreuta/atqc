import pickle

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
        self.__experience = 0
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

#Task 1.1 Define wait method

    def wait(self):
        self.__health = round(self.__health * 1.1)
        self.__strength = round(self.__strength * 1.1)
        self.make_sound("I'm waiting, My strenght now is {} and health is {}".format(
            self.__strength,
            self.__health
        ))

# Task 1.2 Save to file(info/object)
# Restore from file

    def save(self, filename):
        f = open(filename, 'w')
        f.write(self.__name + ": My strenght now is {} and health is {}".format(
            self.__strength,
            self.__health
        ))
        f.close()

    def save1(self, filename):
        f = open(filename, 'wb')
        pickle.dump(self,f)
        f.close()
        print('{} saved'.format(self.__name))


    def restore(self, filename):
        f = open(filename, 'rb')
        obj = pickle.load(f)
        self.__dict__.update(obj.__dict__)
        f.close()
        print('{} restored'.format(self.__name))


# Task 1.2 Define property "Experience"

        @property
        def experience(self):
            return self.__experience

        @experience.setter
        def experience(self, damage):
            if enemy.is_dead():
                self.__experience = round(damage * 1.1)



# Task 2: Add subclasses Elf, Gnome, Orc

class Elf(Warrior):        
    def __init__(self, name):
        Warrior.__init__(self, name, hsfactor=0.3)
        self.make_sound = ("I'm Elf!")
  

class Gnome(Warrior):
    def __init__(self, name):
        Warrior.__init__(self, name, hsfactor=0.5)
        self.make_sound = Warrior.make_sound


class Orc(Warrior):
    def __init__(self, name, hsfactor=0.7):
        super(Orc, self).__init__(name)

    def attack(self, enemy):
        super(Orc, self).attack(enemy, damage = 10)


# import importlib
# importlib.reload(battle)