class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.hp = 100
    
    def to_dict(self):
        return {
            'name': self.name,
            'inventory': self.inventory,
            'hp': self.hp
        }
