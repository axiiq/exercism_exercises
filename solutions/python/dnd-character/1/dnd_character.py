import random

class Character:
    def ability(self):
        output = []
        for i in range(4):
            output.append(random.randint(1,6))
        output.sort(reverse=True)
        return sum(output[0:3])

    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()

        self.hitpoints = 10 + modifier(self.constitution)

        
        

def modifier(value):
    return (value - 10) // 2
