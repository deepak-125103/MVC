from abc import ABC, abstractmethod
from models.invoices import Invoices

class A_invoices(ABC):

    @abstractmethod
    def create_invoices(self, model: Invoices)-> None:
        pass

    @abstractmethod
    def update_invoices(self, inv_id: int, model: Invoices)->None:
        pass

    @abstractmethod
    def delete_invoices(self,inv_id: int)-> None:
        pass

    @abstractmethod
    def get_invoices(self, inv_id: int)-> Invoices:
        pass

    @abstractmethod
    def get_all_invoices(self)->list[Invoices]:
        pass