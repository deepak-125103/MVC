from abc import ABC, abstractmethod
from models.customers import Customer

class A_Customer(ABC):
    @abstractmethod
    def create_customer(self,model: Customer)->None:
        pass
    @abstractmethod
    def update_customer(self,customer_id:int,model:Customer)->None:
        pass

    @abstractmethod
    def delete_customer(self,customer_id:int,model:Customer)-> None:
        pass
    
    @abstractmethod
    def get_customer(self,customer_id:int)-> Customer:
        pass
    
    @abstractmethod
    def get_all_customer(self)->list[Customer]:
        pass
