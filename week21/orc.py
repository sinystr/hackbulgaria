from entity import Entity


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        if berserk_factor < 1:
            self.berserk_factor = 1
        elif berserk_factor > 2:
            self.berserk_factor = 2
        else:
            self.berserk_factor = berserk_factor

    def attack(self):
        return super().attack() * self.berserk_factor
