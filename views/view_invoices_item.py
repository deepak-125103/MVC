from models.repos.invoice_items_repo import invo_item_repo
from models.invoice_items import Invoice_items

def view_create_invoices_item():
    invoice_item_id=input("1. Enter Invoices item ID :")
    invoice_id=input("Enter Invoice ID :")
    Track_id=input("Enter Track ID :")
    Unit_Price=input("Enter Unit Price :")
    Quantity=input("Enter Quantity :")
    new_Invoice_item=Invoice_items(invoice_item_id,invoice_id,Track_id,Unit_Price,Quantity)
    itr=invo_item_repo()
    itr.create_invoice_items(new_Invoice_item)
    view_all_invo_item()

def view_update_invoice_item():
    invoice_item_id=input("2. Enter Invoices item ID :")
    invoice_id=input("Enter Invoice ID :")
    Track_id=input("Enter Track ID :")
    Unit_Price=input("Enter Unit Price :")
    Quantity=input("Enter Quantity :")
    update_inv=Invoice_items(invoice_item_id,invoice_id,Track_id,Unit_Price,Quantity)
    itr=invo_item_repo()
    itr.update_invoice_items(invoice_item_id,update_inv)
    view_all_invo_item()

def view_delete_invoice_item():
    invoice_item_id=input("3. Enter Invoices item ID : ")
    inv_del=invo_item_repo()
    inv_del.delete_Invoice_items(invoice_item_id)
    view_all_invo_item()

def view_all_invo_item():
    '''Fetches and display all invoices items '''
    try:
        ai=invo_item_repo()
        aii=ai.get_all_Invoice_items()
        if not aii:
            print("No invoices items found")
        else:
            print("Data list \n----")
            for li in aii:
                print(f"Items ID:{li.invoice_item_id}, inoice id:{li.invoice_id},Track ID:{li.Track_id}, Unit Price: {li.Unit_Price}, Quantity:{li.Quantity}")
    except Exception as e:
        print(f"an error occurred: {e}")


def view_invo_items(inv_items_id:int):
    '''Fetch and display invoice items with ID'''
    try:
        invo=invo_item_repo()
        in_item=invo.get_Invoice_items(inv_items_id)
        if in_item:
            print(f"Items ID:{in_item.invoice_item_id}, inoice id:{in_item.invoice_id},Track ID:{in_item.Track_id}, Unit Price: {in_item.Unit_Price}, Quantity:{in_item.Quantity}")
        else:
            print("No invoices found")
    except Exception as e:
        print(f"An error ocuured by {e}")

if __name__=="__main__":
    print("choose an option")
    print("Press 1. for Create invoice item :")
    print("Press 2. for Update invoice item :")
    print("Press 3. for Delete invoice item :")
    print("Press 4. for all invoices items :")
    print("Press 5. for get single invoice item :")
    choice=input("Enter your Choice")
    if choice=="1":
        view_create_invoices_item()
    elif choice=="2":
        view_update_invoice_item()
    elif choice=="3":
        view_delete_invoice_item()
    elif choice=="4":
        view_all_invo_item()
    elif choice=="5":
        try:
            inv_items_id=int(input("Enter invoice item ID: "))
            view_invo_items(inv_items_id)
        except ValueError:
            print("invalid ID please enter numerical id")
    else:
        print("Invalid choice choose an option between 1 to 2")