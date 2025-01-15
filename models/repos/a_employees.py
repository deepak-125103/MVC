from abc import ABC, abstractmethod
from models.employees import Employees

class A_emp(ABC):
    @abstractmethod
    def create_employee(self,model:Employees)-> None:
        pass
    @abstractmethod
    def update_employee(self, Emp_id: int, model: Employees)-> None:
        pass

    @abstractmethod
    def delete_employee(self, Emp_id: int, model: Employees)-> None:
        pass
    @abstractmethod
    def get_employee(self, Emp_id: int)-> Employees:
        pass

    @abstractmethod
    def get_all_employee(self)->list[Employees]:
        pass