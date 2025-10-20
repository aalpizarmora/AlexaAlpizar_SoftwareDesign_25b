from src.models.armor import Armor

class LeatherArmor(Armor):
    def reduce_damage(self, damage):
        return max(0, damage - 5)
    
    def get_name(self):
        return "Armadura de Cuero"