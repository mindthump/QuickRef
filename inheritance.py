# coding=utf-8

class Seaman(object):
    """
    A Superclass, provides default fields and methods
    """

    def __init__(self, name):
        self.data = {
            'name': name,
            'sound': "Land Ho!"
        }

    @property
    def sound(self):
        return self.data['sound']

    @sound.setter
    def sound(self, value):
        self.data['sound'] = value

    @property
    def name(self):
        return self.data['name']

    def talk(self):
        print "{} says: {}".format(self.name, self.sound)


class Sailor(Seaman):
    def __init__(self, name):
        super(Sailor, self).__init__(name)
        self.sound = "Hoist the Mainsail!"


class Pirate(Seaman):
    def __init__(self, name):
        super(Pirate, self).__init__(name)
        self.sound = "Aaarrrgggh!"

    def talk(self, loud=False):
        super(Pirate, self).talk()
        if loud:
            print("...AND A YO HO HO!!!")


if __name__ == '__main__':
    the_pirate = Pirate('Peg-leg Pete')
    the_pirate.talk()
    kidd = Pirate("Captain Kidd")
    kidd.talk(True)
    the_sailor = Sailor('Billy Budd')
    the_sailor.talk()
    popeye = Sailor("Popeye")
    popeye.sound = "I yam what I yam!"
    popeye.talk()
    gilligan = Seaman("Gilligan")
    gilligan.talk()
