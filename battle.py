import random
import pickle


class Warrior():
    '''
    Warrior is a base class for all wariors in the Battle.
    Use it to construct your own special Warrior Types
    '''

    # Power is the whole amount of energy that the warrior has.
    # It is distributed between
    # strength and health according to the hsfactor:
    # strength = __power * hsfactor
    # health   = __power * (1 - hsfactor)
    _power = 100
    _mess = {
        "born": "I've been born! My strenght is {} and health is {}",
        "hard": "It's too hard to me...",
        "hit": "Taste my {}-power hit!",
        "oh!": "Oh!",
        "...": "...",  # Dead sound
        "fine": "I'm fine, tnx! My strength is {} and health is {}",
        "wait": "I'm waiting, my strength now is {} and health is {}",
        "saved": "{} saved to file",
        "restored": "{} restored form file",
    }

    def __init__(self, name, hsfactor=0.5):
        self._name = name.upper()
        self._health = round(type(self)._power * hsfactor)
        self._strength = round(type(self)._power * (1 - hsfactor))
        self._exp = 0
        power = self._health + self._strength  # must be 1 after rounding
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

    def attack(self, enemy, damage):
        if self.is_dead():
            print("GOD: {} is dead. I'm sorry...".format(self._name))
            return

        if damage > self._strength:
            self.make_sound(type(self)._mess["hard"])
            return
        self.make_sound(type(self)._mess["hit"].format(damage))

        enemy_was_alive = not enemy.is_dead()
        enemy.defend(damage + round(damage * self._exp * 10 / 100))
        if enemy_was_alive and enemy.is_dead(): self._exp += 1

        self._strength -= damage

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

    # Task 1.1 Define wait method

    def wait(self):
        self._health = round(self._health * 1.1)
        self._strength = round(self._strength * 1.1)
        self.make_sound(type(self)._mess["wait"].format(
            self._strength,
            self._health
        ))

    # Task 1.2 Save to file/restore from file
    # Restore from file

    def save(self, filename):
        f = open(filename, 'wb')
        pickle.dump(self, f)
        f.close()
        self.make_sound(type(self)._mess["saved"].format(self._name))

    def restore(self, filename):
        f = open(filename, 'rb')
        obj = pickle.load(f)
        self.__dict__.update(obj.__dict__)
        f.close()
        self.make_sound(type(self)._mess["restored"].format(self._name))


class Orc(Warrior):
    _mess = {
        "born": "OOOOrc!!! {}/{}",
        "hard": "No. Weak",
        "hit": "Hrrrakh!!! {}",
        "oh!": "Uuuu...",
        "...": "Ooops, it seems I'm dead X_X",  # Dead sound
        "fine": "Ha-ha! {}/{}",
        "wait": "I'm waiting, my strength now is {} and health is {}",
        "saved": "{} saved to file",
        "restored": "{} restored form file",
    }

    def __init__(self, name):
        super().__init__(name, hsfactor=0.7)

    def attack(self, enemy):
        super().attack(enemy, damage=10)


class Elf(Warrior):
    _mess = {
        "born": "A New Elf has been born! {} - {}",
        "hard": "Not enough magic...",
        "hit": "Get my magic sword! {} ",
        "oh!": "Yes, it's hurt...",
        "...": " Ooops, it seems I'm dead X_X",  # Dead sound
        "fine": "Great! {}/{}",
        "wait": "I'm waiting, my strength now is {} and health is {}",
        "saved": "{} saved to file",
        "restored": "{} restored form file",
    }

    def __init__(self, name):
        super().__init__(name, hsfactor=0.3)

    def attack(self, enemy):
        damage = random.randint(
            round(0.1 * self._strength),
            self._strength)
        super().attack(enemy, damage)


class Gnome(Warrior):
    _mess = {
        "born": "Gnome. {}*{}",
        "hard": "No.",
        "hit": "Hit. {} ",
        "oh!": "@d.$A!",
        "...": " Ooops, it seems I'm dead X_X",  # Dead sound
        "fine": "{}*{}",
        "wait": "I'm waiting, my strength now is {} and health is {}",
        "saved": "{} saved to file",
    }

    def __init__(self, name):
        super().__init__(name, hsfactor=0.5)

    def attack(self, enemy):
        damage = round(0.25 * self._strength)
        super().attack(enemy, damage)


class Battle:
    def __init__(self, w1, w2):
        self.__w1 = w1
        self.__w2 = w2

    def fight(self):
        while not (self.__w1.is_dead() or self.__w2.is_dead()):
            self.__w1.attack(self.__w2)
            self.__w2.attack(self.__w1)
        winnew = ''
        if self.__w2.is_dead():
            winnew = self.__w1.name
        elif self.__w1.is_dead():
            winnew = self.__w2.name
        print("The winner is: " + winnew)

