# tests/test_armor.py
import unittest
from src.models.character import Character
from src.models.leather_armor import LeatherArmor
from src.models.plate_armor import PlateArmor

class TestArmorSystem(unittest.TestCase):
    
    def test_leather_armor_reduces_damage(self):
        character = Character("Guerrero")
        armor = LeatherArmor()
        character.equip_armor(armor)
        
        damage_reduced = character.take_damage(15)
        
        self.assertEqual(character.health, 90)  # 100 - (15 - 5) = 90
        self.assertEqual(armor.get_name(), "Armadura de Cuero")
    
    def test_plate_armor_better_protection(self):
        character = Character("Paladín")
        armor = PlateArmor()
        character.equip_armor(armor)
        
        damage_reduced = character.take_damage(15)
        
        self.assertEqual(character.health, 95)  # 100 - (15 - 10) = 95
        self.assertEqual(armor.get_name(), "Armadura de Placas")