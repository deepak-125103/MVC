from abc import ABC, abstractmethod
from models.playlists import Playlist

class A_playlist(ABC):
    @abstractmethod
    def create_palylist(self, model: Playlist)-> None:
        pass
    
    @abstractmethod
    def upadate_playlist(self, pl_id: int, model:  Playlist)-> None:
        pass

    @abstractmethod
    def delete_playlist(self,pl_id: int)-> None:
        pass

    @abstractmethod
    def get_playlist(self, pl_id: int)-> Playlist:
        pass

    @abstractmethod
    def get_all_palylist(self,pl_id:int)->list[Playlist]:
        pass
