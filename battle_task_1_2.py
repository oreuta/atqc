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
    
    __mess = {
        "born": "I've been born! My strenght is {} and health is {}",
        "hard": "It's too hard to me...",
        "hit": "Taste my {}-power hit!",
        "oh!": "Oh!", 
        "...": "...", # Dead sound
        "fine": "I'm fine, tnx! My strength is {} and health is {}",
    }
    
    @classmethod
    def get_power(cls):
        return cls.__power
    
    def __init__(self, name, hsfactor = 0.5):
        self.__name = name.upper()
        self.__health = round(self.get_power() * hsfactor)
        self.__strength = round(self.get_power() * (1 - hsfactor))
        self.__experience = 0
        power = self.__health + self.__strength # must be 1 after rounding
        if power > 1:
            self.__health - 1
        elif power < 1:
            self.__health + 1
        self.make_sound(type(self).__mess["born"].format(
            round(self.__strength),
            round(self.__health)
        ))
    @property
    def name(self):
        return self.__name
    
    def is_dead(self):
        return self.__health <= 0

    def make_sound(self, sound):
        print("{}: {}".format(self.__name, sound))

    def wait(self, increase=1.1):
        self.__health = self.__health*increase
        self.__strength = self.__strength*increase
        print ("Attack is skipped for {}. Health is {}, strength is {}".format(self.__name, round(self.__health), round(self.__strength)))
    
    def attack(self, enemy, damage):
        if self.is_dead():
            print("GOD: {} is dead. I'm sorry...".format(self.__name))
            return
        
        skip = input("{}, do you want to skip the attack? (y/n) ".format(enemy.__name))
        while (skip!="y" and skip!="n"):
            skip = input("Please, make your choise: y/n ")
               
        if skip == "y":
            return enemy.wait()
        if skip == "n":
            if damage > self.__strength:
                self.make_sound(type(self).__mess["hard"])
                return
            
            if self.__experience == 0:    
                self.make_sound(type(self).__mess["hit"].format(damage))
                self.__experience += 1
                enemy.defend(damage)
                self.__strength -= damage
                
            else:
                self.make_sound(type(self).__mess["hit"].format(int(damage*1.1)))
                self.__experience += 1
                enemy.defend(damage*1.1)
                self.__strength -= (damage*1.1)
        
    def defend(self, damage):
        self.__health -= damage
        if self.is_dead():
            self.make_sound(type(self).__mess["..."])
        else:
            self.make_sound(type(self).__mess["oh!"])

    def how_are_you(self):
        self.make_sound(type(self).__mess["fine"].format(
            self.__strength,
            self.__health
        ))
        
    def save(self):
        '''
        import shelve
        my_file = shelve.open("{}.py".format(self.__name), "c")
        my_file["Name"] = ["{}".format(self.__name)]
        my_file["Strength"] =  ["{}".format(self.__strength)]
        my_file["Health"] = ["{}".format(self.__health)]
        my_file["Experience"] = ["{}".format(self.__experience)]
        my_file["Hsfactor"] = ["{}".format(self.__hsfactor)]
        my_file.close()
        '''
        
        my_file=open("{}.py".format(self.__name), "w")
        my_file.write("My name is {},\n My health is {}, \n My stength is {}, \n My experience is {}.".format(self.__name, self.__health, self.__strength, self.__experience))
        my_file.close()

    def restore(self):
        f = open("{}.py".format(self.__name))
        f.readlines()
        print("{} is back! My health is {}, my strength is {}, my experience is {}.".format(self.__name, round(self.__health), round(self.__strength), self.__experience))


class Elf(Warrior):
    __mess = {
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
    __mess = {
        "born": "I'm Orc. Health: {}/ Strength: {}",
        "hard": "No. Weak",
        "hit": "Hit! {} ",
        "oh!": "Uuuuu...",
        "...": " .o. ",
        "fine": "Ha-ha! {}/{}",
        }
    
    def __init__(self, name, hsfactor = 0.5):
        super(Gnome, self).__init__(name, hsfactor = 0.5)
        
    def attack(self, enemy):
        damage = round(0.25 * type(self).__strength)  #надо достучаться до силы гнома но как???? не выходит через этот атрибутоно пытается вытащить у гнома но через дикт видно что харится то все у Вариора
        super(Gnome, self).attack(enemy, damage)

    def make_sound(self, sound):
        super(Gnome, self).make_sound(sound)
        
class Orc(Warrior):
    __mess = {
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
        self.__w1 = w1
        self.__w2 = w2


    def fight(self):
        while not (self.__w1.is_dead() or self.__w2.is_dead()):
            self.__w1.attack(self.__w2)
            self.__w2.attack(self.__w1)
        
        winner = self.__w1 if self.__w2.is_dead() else self.__w2
        print("GOD: This time {} was more lucky!".format(winner.name))
        
        
        
        
        

        
        



    





    

