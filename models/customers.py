class Customer:
    def __init__(self,customer_id: int, first_name:str, last_name:str, company:str, address: str, city: str, state: str, country: str, Postal_code:str, phone: str, fax:str, email:str, support_repid: int):
        self.customer_id=customer_id
        self.first_name=first_name
        self.last_name=last_name
        self.company=company
        self.city=city
        self.address=address
        self.state=state
        self.country=country
        self.Postal_code=Postal_code
        self.phone=phone
        self.fax=fax
        self.email=email
        self.support_repid=support_repid

    def __repr__(self):
         return f"Customer(customer_id:{ self.customer_id}, first name:{self.first_name},last name:{self.first_name},company:{ self.company}, address:{self.address},city:{self.city},state:{self.state},country:{self.country},Postal code:{self.Postal_code},phone:{self.phone},fax:{self.fax},email:{self.email},support repid:{self.support_repid})"