from src.models.armor import Armor

class PlateArmor(Armor):
    def reduce_damage(self, damage):
        return max(0, damage - 10)
    
    def get_name(self):
        return "Armadura de Placas"
