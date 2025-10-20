class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.is_alive = True
        self.armor = None
    
    def take_damage(self, damage):
        actual_damage = damage
        if self.armor:
            actual_damage = self.armor.reduce_damage(damage)
            
        self.health -= actual_damage
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            
        return actual_damage
    
    def heal(self, amount):
        if self.is_alive:
            self.health += amount
            
    def equip_armor(self, armor):
        self.armor = armor
        return f"{self.name} equipó {armor.get_name()}"

    def unequip_armor(self):
        if self.armor:
            armor_name = self.armor.get_name()
            self.armor = None
            return f"{self.name} removió {armor_name}"
        return f"{self.name} no tiene armadura equipada"