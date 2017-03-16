class Warrior():
    '''
    Warrior is a base class for all wariors in the Battle.
    Use it to construct your own special Warrior Types
    '''
    import random
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

    def wait(self, increase=1.1):
        self.__health = self.__health*increase
        self.__strength = self.__strength*increase
        print ("Attack is skipped for {}. Health is {}, strength is {}".format(self.__name, round(self.__health), round(self.__strength)))
    
    def attack(self, enemy, damage):
        A = input("{}, do you want to skip the attack? (y/n) ".format(enemy.__name))

        
        while (A!="y" and A!="n"):
            A = input("Please, make your choise: y/n ")
            
        
        if A == "y":
            return enemy.wait()
        if A == "n":
            if self.is_dead():
                print("GOD: {} is dead. I'm sorry...".format(self.__name))
                return
            if damage > self.__strength:
                make_sound("It's too hard to me...")
                return
            if self.__experience == 0:    
                self.make_sound("Taste my {}-power hit!".format(damage))
                self.__experience += 1
                enemy.defend(damage)
                self.__strength -= damage
                
            else:
                self.make_sound("Taste my {}-power hit!".format(int(damage*1.1)))
                self.__experience += 1
                enemy.defend(damage*1.1)
                self.__strength -= (damage*1.1)
        
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
        
    def save(self):
        my_file=open("{}.py".format(self.__name), "w")
        my_file.write("My name is {},\n My health is {}, \n My stength is {}, \n My experience is {}.".format(self.__name, self.__health, self.__strength, self.__experience))
        my_file.close()

    def restore(self):
        f = open("{}.py".format(self.__name))
        f.readlines()
        print("{} is back! My health is {}, my strength is {}, my experience is {}.".format(self.__name, self.__health, self.__strength, self.__experience))


class Elf(Warrior):
    def __init__(self, name, hsfactor = 0.3):
        super(Elf, self).__init__(name, hsfactor = 0.3)
        '''
        self.make_sound("I'm ELF! My strenght is {} and health is {}".format(
            round(self.__strength),
            round(self.__health)
        ))
   '''
    import random
    d = random.randint(1,100)
    def attack(self, enemy, damage = d):
        super(Elf, self).attack(enemy, damage)

    def make_sound (self, sound):
        super(Elf, self).make_sound(sound)
        

class Gnome(Warrior):
    def __init__(self, name, hsfactor = 0.5):
        super(Gnome, self).__init__(name, hsfactor = 0.5)
    
    def attack(self, enemy, damage = None):
        if damage == None:
            damage=0.25*self.__strength*100
        super(Gnome, self).attack(enemy, damage)

        
    def make_sound (self, sound):
        super(Gnome, self).make_sound(sound)

class Orc(Warrior):
    def __init__(self, name, hsfactor = 0.7):
        super(Orc, self).__init__(name, hsfactor = 0.7)

    def attack(self, enemy, damage = 10):
        super(Orc, self).attack(enemy, damage)

    def make_sound (self, sound):
        super(Elf, self).make_sound(sound)
        
        
        
        
        

        
        



    





    

