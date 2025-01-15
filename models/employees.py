class Employees:
    def __init__(self, employee_id: int, fist_name: str, last_name:str, title: str, reports_to:int, birth_date:str, hire_date:str, address:str,city:str,country:str,Postal_code:str,phone:int,fax:str,email:str,state:str):
        self.employee_id=employee_id
        self.fist_name=fist_name
        self.last_name=last_name
        self.title=title
        self.reports_to=reports_to
        self.birth_date=birth_date
        self.hire_date=hire_date
        self.address=address
        self.city=city
        self.country=country
        self.Postal_code=Postal_code
        self.phone=phone
        self.fax=fax
        self.email=email
        self.state=state
        

    def __repr__(self):
        return f"Employees(Emp. ID: {self.employee_id}, First Name:{ self.fist_name}, Last Name:{self.last_name}, Title:{self.title}, ReportsTo:{ self.reports_to}, Birth Date:{self.birth_date}, Hire Date:{self.hire_date}, Address:{self.address},city:s{self.city},country:{self.country},Postal_code:{self.Postal_code},phone:{self.phone},fax:{self.fax},email:{self.email},state:{self.state})"