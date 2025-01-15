from abc import ABC, abstractmethod
from models.artists import Artist

class A_artist(ABC):
    @abstractmethod
    def creat_artist(self,model: Artist)-> None:
        pass

    @abstractmethod
    def update_artist(self, ar_id: int, model: Artist)-> None:
        pass

    @abstractmethod
    def delet_artist(self,ar_id: int)-> None:
        pass

    @abstractmethod
    def get_artist(self,ar_id: int)->Artist:
        pass

    @abstractmethod
    def get_all_artist(self)->list[Artist]:
        pass