from abc import ABC, abstractmethod
from models.playlist_track import Playlist_Track

class A_pl_track(ABC):
    @abstractmethod
    def creat_playlist_track(self,model:Playlist_Track)-> None:
        pass


    @abstractmethod
    def update_playlist_track(self,playlist_track_id: int, track_id:int, model: Playlist_Track)-> None:
        pass
    
    
    @abstractmethod
    def delete_playlist_track(self,plt_id: int, t_id:int)-> None:
        pass
    
    
    @abstractmethod
    def get_playlist_track(self,plt_id: int, t_id:int)->Playlist_Track:
        pass
    
    
    @abstractmethod
    def get_all_playlist_track(self)->list[Playlist_Track]:
        pass
