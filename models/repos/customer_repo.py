from models.customers import Customer
from models.repos.a_customers import A_Customer
import sqlite3

class Customer_repo():
    def create_customer(self,model: Customer)->None:
        try:
            with sqlite3.connect("chinook.db")as conn:
                conn.execute(f" insert into customers values({model.customer_id},'{model.first_name}','{model.last_name}','{model.company}','{model.city}','{model.address}','{model.state}','{model.country}','{model.Postal_code}','{model.phone}','{model.fax}','{model.email}','{model.support_repid}')")
        except sqlite3.Error as e:
            print(f"Database Error: {e}")

        
   
    def update_customer(self,customer_id:int,model:Customer)->None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"update customers set FirstName= '{model.first_name}',  LastName='{model.last_name}',Company='{model.company}',Address='{model.address}',City='{model.city}',State='{model.state}',Country='{model.country}',PostalCode='{model.Postal_code}',Phone='{model.phone}',Fax='{model.fax}',Email='{model.email}',SupportRepId={model.support_repid} WHERE CustomerId={customer_id}")
        except sqlite3.Error as e:
            print(f"Database Error {e}")


    
    def delete_customer(self,customer_id:int)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"delete from customers WHERE CustomerId={customer_id}")
        except sqlite3.Error as e:
            print(f"Databse Error {e}")
    
    
    def get_customer(self,customer_id:int)-> Customer:
        try:
            conn=sqlite3.connect("chinook.db")
            print("Data base is connected successfully")
            cursor=conn.execute("select * from customers WHERE CustomerId=?",(customer_id,))
            row=cursor.fetchone()
            if row:
                return Customer(customer_id=row[0], first_name=row[1], last_name=row[2], company=row[3], address=row[4], city=row[5], state=row[6],country=row[7],Postal_code=row[8],phone=row[9],fax=row[10], email=row[11], support_repid=row[12])
            else:
                print(f"no customer found {customer_id}")
                return None
        except sqlite3.Error as e:
            print(f"Database error {e}")
            return None
        finally:
            conn.close()


    def get_all_customer(self)->list[Customer]:
        data_list=[]
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor=conn.execute("select *from customers")
                for row in cursor:
                    gc=Customer(customer_id=row[0], first_name=row[1], last_name=row[2], company=row[3], address=row[4], city=row[5], state=row[6],country=row[7],Postal_code=row[8],phone=row[9],fax=row[10], email=row[11], support_repid=row[12])
                    data_list.append(gc)
        except sqlite3.Error as e:
            print(f"Databse error as {e}")
        return data_list