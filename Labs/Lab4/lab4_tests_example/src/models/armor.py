from abc import ABC, abstractmethod

class Armor(ABC):
    @abstractmethod
    def reduce_damage(self, damage):
        pass

    @abstractmethod
    def get_name(self):
        pass