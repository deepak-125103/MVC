from models.invoice_items import Invoice_items
from models.repos.a_invoices_items import A_invo_tiems
import sqlite3

class invo_item_repo(A_invo_tiems):
    def create_invoice_items(self, model: Invoice_items)-> None:
        try:
            with sqlite3.connect("chinook.db")  as conn:
                conn.execute(f"insert into invoice_items values('{model.invoice_item_id}','{model.invoice_id}','{model.Track_id}','{model.Unit_Price}','{model.Quantity}')")
        except sqlite3.Error as e:
            print(f"Databse Error {e}")

    def update_invoice_items(self, inv_items_id: int, model: Invoice_items)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"update invoice_items set InvoiceId='{model.invoice_id}', TrackId='{model.Track_id}', UnitPrice='{model.Unit_Price}', Quantity='{model.Quantity}' where InvoiceLineId={inv_items_id}")
        except sqlite3.Error as e:
            print(f"Data base Error {e}")

    def delete_Invoice_items(self, inv_items_id: int)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f" delete from invoice_items where InvoiceLineId={inv_items_id}")
        except sqlite3.Error as e:
            print(f"Data base Error {e}")

    def get_Invoice_items(self, inv_items_id:int)-> Invoice_items:
        try:
            conn=sqlite3.connect("chinook.db")
            print("Data base is connected successfully")
            cursor= conn.execute("select * from invoice_items WHERE InvoiceLineId=?",(inv_items_id,))
            row=cursor.fetchone()
            if row:
                return Invoice_items(invoice_item_id=row[0], invoice_id=row[1], Track_id=row[2], Unit_Price=row[3], Quantity=row[4])
            else:
                print(f"No data base found with ID {inv_items_id}")
                return None
        except sqlite3.Error as e:
            print(f"Database error as {e}")
            return None
        finally:
            conn.close()



    def get_all_Invoice_items(self)-> list[Invoice_items]:
        data_list= []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor= conn.execute("select * from Invoice_items")
                for row in cursor:
                    Gii= Invoice_items(invoice_item_id=row[0], invoice_id=row[1], Track_id=row[2], Unit_Price=row[3], Quantity=row[4])
                    data_list.append(Gii)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list