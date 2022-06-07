from decouple import config

class Rarity:
    def __init__(self, valor):
        self.id = id
        self.name = valor
       
    
    def convert_to_json(self):
        return {
            'id': self.id,
            'name': self.valor
        }
    def __repr__(self, rarity):
        return f"{rarity.id}//{rarity.valor}//\n"