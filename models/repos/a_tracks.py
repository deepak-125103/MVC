from abc import ABC,abstractmethod
from models.tracks import Track

class A_Track(ABC):
    @abstractmethod
    def creat_tracks(self,model:Track )-> None:
        pass
    
    @abstractmethod
    def update_tracks(self, tr_id: int, model:Track)-> None:
        pass

    @abstractmethod
    def delete_track(self, tr_id: int)-> None:
        pass

    @abstractmethod
    def get_track(self,tr_id: int)-> Track:
        pass
    @abstractmethod
    def get_all_track(self)-> Track:
        pass
        
