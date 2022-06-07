from decouple import config

class Role:
    def __init__(self, val):
        self.id = id
        self.name = val
       
    
    def convert_to_json(self):
        return {
            'id': self.id,
            'name': self.val
        }
    def __repr__(self, role):
        return f"{role.id}//{role.val}//\n"
    