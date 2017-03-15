#This simple program for self-training has been created using Warrior.py as example

#health = 100% by default, if it 0 or less-->die
#figther has 3 characteristics: strength, speed, health

class Fighter():

    print("For the fight we need two fighters!")
    print("Welcome them: \n"
          "To call a fighter specify Fighter's Name, Strength, Speed in format elf = Fighter('Legolas', 500, 500)")

    def __init__(self, name, strength, speed):
        self.__name = name.upper()
        self.__health = 100
        self.__strength = strength
        self.__speed = speed
        self.__power = self.__speed * self.__strength
        print("A new figther - "+name.upper()+" joined us!")
        self.check_parameters()

    def check_parameters(self):
        print("----------------------------------------------- \n"
              "Name of hero: {}".format(self.__name) +"\n"
              "Strength: {}".format(self.__strength) +"\n"
              "Speed: {}".format(self.__speed) +"\n"
              "Health: {:.2f} %".format(self.__health))

    @property
    def health(self):
        return self.__health

    def attack(self, enemy, damage):
        if self.__health <= 0:
            self.make_sound("Oh... I have already died!")
            return

        self.make_sound("I'll take {} of your power!".format(damage))
        enemy.defend(damage)
        if enemy.health <= 0:
            self.make_sound("My enemy was defeated!")
            self.check_parameters()
        else:
            self.make_sound("You will die soon!")
        return

    def defend(self, damage):
        self.__health -= damage * 100 / self.__power
        if self.__health < 0:
            self.__health = 0
            self.make_sound("I died...")
            self.check_parameters()
        else:
            self.make_sound("My health is decreased... only {:.2f} % left.".format(self.__health))
        return
        
    def make_sound(self, sound):
        print("{}: {}".format(self.__name, sound))

