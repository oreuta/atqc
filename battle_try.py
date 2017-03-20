import shelve

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
    _power = 100
    
    _mess = {
        "born": "I've been born! My strenght is {} and health is {}",
        "hard": "It's too hard to me...",
        "hit": "Taste my {}-power hit!",
        "oh!": "Oh!", 
        "...": "...", # Dead sound
        "fine": "I'm fine, tnx! My strength is {} and health is {}",
    }
    
    @classmethod
    def get_power(cls):
        return cls._power
    
    def __init__(self, name, hsfactor = 0.5):
        self._name = name.upper()
        self._health = round(self.get_power() * hsfactor)
        self._strength = round(self.get_power() * (1 - hsfactor))
        self._experience = 0
        power = self._health + self._strength # must be 1 after rounding
        if power > 1:
            self._health - 1
        elif power < 1:
            self._health + 1
        self.make_sound(type(self)._mess["born"].format(
            round(self._strength),
            round(self._health)
        ))
    @property
    def name(self):
        return self._name
    
    def is_dead(self):
        return self._health <= 0

    def make_sound(self, sound):
        print("{}: {}".format(self._name, sound))

    def wait(self, increase=1.1):
        self._health = self._health*increase
        self._strength = self._strength*increase
        print ("Attack is skipped for {}. Health is {}, strength is {}".format(self._name, round(self._health), round(self._strength)))
    
    def attack(self, enemy, damage):
        if self.is_dead():
            print("GOD: {} is dead. I'm sorry...".format(self._name))
            return
        
        skip = input("{}, do you want to skip the attack? (y/n) ".format(enemy._name))
        while (skip!="y" and skip!="n"):
            skip = input("Please, make your choise: y/n ")
               
        if skip == "y":
            return enemy.wait()
        if skip == "n":
            if damage > self._strength:
                self.make_sound(type(self)._mess["hard"])
                return
            
            if self._experience == 0:    
                self.make_sound(type(self)._mess["hit"].format(damage))
                self._experience += 1
                enemy.defend(damage)
                self._strength -= damage
                
            else:
                self.make_sound(type(self)._mess["hit"].format(int(damage*1.1)))
                self._experience += 1
                enemy.defend(damage*1.1)
                self._strength -= (damage*1.1)
        
    def defend(self, damage):
        self._health -= damage
        if self.is_dead():
            self.make_sound(type(self)._mess["..."])
        else:
            self.make_sound(type(self)._mess["oh!"])

    def how_are_you(self):
        self.make_sound(type(self)._mess["fine"].format(
            self._strength,
            self._health
        ))
        
    def save(self):
        import pickle
        my_file = open("{}.py".format(self._name), 'wb')
        pickle.dump(self, my_file)
        my_file.close()
        
        ''' second type - incorrect type of file
        import shelve
        my_file = shelve.open('{}.py'.format(self._name), "n")
        my_file["Name"] = ["{}".format(self._name)]
        my_file["Strength"] =  ["{}".format(self._strength)]
        my_file["Health"] = ["{}".format(self._health)]
        my_file["Experience"] = ["{}".format(self._experience)]
        my_file.close()
        '''
        ''' first try
        my_file=open("{}.py".format(self._name), "w")
        my_file.write("My name is {},\n My health is {}, \n My stength is {}, \n My experience is {}.".format(self._name, self._health, self._strength, self._experience))
        my_file.close()
        '''

    
    def restore(self):
        import pickle
        
        my_file = open("{}.py".format(self.name), 'rb')
        obj = pickle.load(my_file)
        self.__dict__.update(obj.__dict__)
        f.close()
        ''' first try - coul read from write and pickle method
        f = open("{}.py".format(self._name))
        f.readlines()
        print("{} is back! My health is {}, my strength is {}, my experience is {}.".format(self._name, round(self._health), round(self._strength), self._experience))
        '''


class Elf(Warrior):
    _mess = {
        "born": "Health is {} - strength is {}",
        "hard": "Not enough of magic...",
        "hit": "Get my magic sword!. {} ",
        "oh!": "It's really hurt...",
        "...": " ~~~ ",
        "fine": "Great! {}/{}",
        }
    
    def __init__(self, name, hsfactor = 0.3):
        super(Elf, self).__init__(name, hsfactor = 0.3)
        
    import random
    d = random.randint(1,100)
    def attack(self, enemy, damage = d):
        super(Elf, self).attack(enemy, damage)

    def make_sound(self, sound):
        super(Elf, self).make_sound(sound)

class Gnome(Warrior):
    _mess = {
        "born": "I'm Gnome. Health: {}/ Strength: {}",
        "hard": "No. Weak",
        "hit": "Hit! {} ",
        "oh!": "Uuuuu...",
        "...": " .o. ",
        "fine": "Ha-ha! {}/{}",
        }
    
    def __init__(self, name, hsfactor = 0.5):
        super(Gnome, self).__init__(name, hsfactor = 0.5)
        
    def attack(self, enemy):
        damage = round(0.25 * self._strength)  #надо достучаться до силы гнома но как???? не выходит через этот атрибутоно пытается вытащить у гнома но через дикт видно что харится то все у Вариора
        super(Gnome, self).attack(enemy, damage)

    def make_sound(self, sound):
        super(Gnome, self).make_sound(sound)
        
class Orc(Warrior):
    _mess = {
        "born": "I'm orccccc. Health: {}* Strength: {}",
        "hard": "No. Weak",
        "hit": "Wrack!!. {}",
        "oh!": "Dam",
        "...": " . ",
        "fine": "{}*{}",
        }
    
    def __init__(self, name, hsfactor = 0.7):
        super(Orc, self).__init__(name, hsfactor = 0.7)

    def attack(self, enemy, damage = 10):
        super(Orc, self).attack(enemy, damage)

    def make_sound(self, sound):
        super(Orc, self).make_sound(sound)
        
class Battle:

    def __init__(self, w1, w2):
        self._w1 = w1
        self._w2 = w2


    def fight(self):
        while not (self._w1.is_dead() or self._w2.is_dead()):
            self._w1.attack(self._w2)
            self._w2.attack(self._w1)
        
        if self._w2.is_dead():
            winner = self._w1
        else:
            winner = self._w2
            
        '''winner = self.__w1 if self.__w2.is_dead() else self.__w2'''
        print("GOD: This time {} was more lucky!".format(winner.name))
        
        
        
        
        

        
        



    





    

