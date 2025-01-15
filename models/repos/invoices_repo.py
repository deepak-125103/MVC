from models.invoices import Invoices
from models.repos.a_invoices import A_invoices
import sqlite3

class Invoice_repo(A_invoices):
    def create_invoices(self, model: Invoices)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f" insert into invoices values({model.invoce_id}, {model.customer_id},'{model.invoce_date}','{model.billing_add}','{model.billing_city}','{model.billing_state}','{model.billing_country}','{model.billing_postal_code}',{model.total})")
        except sqlite3.Error as e:
            print(f"Data base error {e}")

    def update_invoices(self, inv_id:int, model: Invoices)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"update invoices set CustomerId={model.customer_id}, InvoiceDate='{model.invoce_date}',BillingAddress='{model.billing_add}',BillingCity='{model.billing_city}',BillingState='{model.billing_state}',BillingCountry='{model.billing_country}',BillingPostalCode='{model.billing_postal_code}',Total={model.total} where InvoiceId ={inv_id}")
        except sqlite3.Error as e:
            print(f"Data base error {e}")

    def delete_invoices(self, inv_id: int)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"delete from invoices where InvoiceId={inv_id}")
        except sqlite3.Error as e:
            print(f"Database Error {e}")

    def get_invoices(self, inv_id: int)-> Invoices:
        try:
            conn=sqlite3.connect("chinook.db")
            print("chinook data base is connected successfully")
            cursor=conn.execute("select * from invoice_items WHERE InvoiceLineId=?",(inv_id,))
            row=cursor.fetchone()
            if row :
                return Invoices(inv_id=row[0],customer_id=row[1],invoce_date=row[2],billing_add=row[3],billing_city=row[4])
            else:
                print(f"No invoice found with id {inv_id}")
                return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            conn.close()

    
    
    def get_all_invoices(self)-> list[Invoices]:
        data_list=[]
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor= conn.execute("select * from invoices")
                for row in cursor:
                    inv= Invoices(invoce_id=row[0], customer_id=row[1], invoce_date=row[2],billing_add=row[3],billing_city=row[4], billing_state=row[5], billing_country=row[6], billing_postal_code=row[7],total=row[8])
                    data_list.append(inv)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list           