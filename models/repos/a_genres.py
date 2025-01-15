from abc import ABC, abstractmethod
from models.genres import Genres

class AGenres(ABC):
    @abstractmethod
    def create_genres(self, model: Genres) -> None:
        pass
    
    @abstractmethod
    def update_genres(self, gener_id: int, model: Genres) -> None:
        pass

    @abstractmethod
    def delete_genres(self, gener_id: int) -> None:
        pass

    @abstractmethod
    def get_genres(self, gener_id: int) ->Genres:
        pass

    @abstractmethod
    def get_all_genres(self) ->list[Genres]:
        pass

    