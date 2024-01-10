class Weapon:
    def __init__(self, name, weapon_type, level):
        self.name = name
        self.weapon_type = weapon_type
        self.level = 1

    def display(self):
        print(self.name + ' ' + self.weapon_type + ' ' + str(self.level))

    def upgrade(self):
        self.level += 1

def run():
    weapon1 = Weapon('Long Sword', 'Sword',1)
    weapon1.display()
    weapon2 = Weapon('Short Spear', 'Spear',1)
    weapon2.display()
    weapon1.upgrade()
    weapon2.upgrade()
    weapon1.display()
    weapon2.display()



