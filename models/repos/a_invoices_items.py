from abc import ABC, abstractmethod
from models.invoice_items import Invoice_items

class A_invo_tiems(ABC):
    @abstractmethod
    def create_invoice_items(self, model: Invoice_items)-> None:
        pass

    @abstractmethod
    def update_invoice_items(self,inv_items_id: int, model:Invoice_items )-> None:
        pass

    @abstractmethod
    def delete_Invoice_items(self,inv_items_id: int)-> None:
        pass

    @abstractmethod
    def get_Invoice_items(self, Inv_id: int)->Invoice_items:
        pass

    @abstractmethod
    def get_all_Invoice_items(self)->list[Invoice_items]:
        pass