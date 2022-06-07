from decouple import config
from . import Role, Rarity

class Footballer():
    def __init__(self, id, name, role, rarity, price, quantity):
        self.id = id
        self.name = name
        self.role = role
        self.rarity = rarity
        self.price = price
        self.quantity = quantity
    
    def convert_to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'role': self.role,
            'rarity': self.rarity,
            'price': self.price,
            'quantity': self.quantity
        }
    def __repr__(self, footballer):
        return f"{footballer.id}//{footballer.name}//{footballer.role}//{footballer.price}//\n"
    
    
    