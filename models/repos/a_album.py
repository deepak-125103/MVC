from abc import ABC,abstractmethod
from models.albums import Album

class abs_album(ABC):
    @abstractmethod
    def create_album(self, model: Album)-> None:
        pass

    @abstractmethod
    def update_album(self, album_id: int, model: Album)-> None:
        pass

    @abstractmethod
    def delete_album(self,album_id:int,model: Album)->None:
        pass

    @abstractmethod
    def get_album(self,album_id:int)-> Album:
        pass

    @abstractmethod
    def get_all_album(self)->list[Album]:
        pass