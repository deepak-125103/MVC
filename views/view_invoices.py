from models.repos.invoices_repo import Invoice_repo
from models.invoices import Invoices

def view_create_invoices():
    invoce_id=input("2. Enter invoice iD : ")
    customer_id=input(" Enter customer ID : ")
    invoce_date=input("Enter invoice date :")
    billing_add=input("Enter billing address :")
    billing_city=input("Enter billing city :")
    billing_state=input("Enter billing state :")
    billing_country=input("Enter billing country :")
    billing_postal_code=input("Enter billing postal code :")
    total=input("Enter total :")
    new_invoices=Invoices(invoce_id,customer_id,invoce_date,billing_add,billing_city,billing_state,billing_country,billing_postal_code,total)
    iir=Invoice_repo()
    iir.create_invoices(new_invoices)
    view_get_all_invoices()

def view_update_invoices():
    invoce_id=input("2. Enter invoice iD : ")
    customer_id=input(" Enter customer ID : ")
    invoce_date=input("Enter invoice date :")
    billing_add=input("Enter billing address :")
    billing_city=input("Enter billing city :")
    billing_state=input("Enter billing state :")
    billing_country=input("Enter billing country :")
    billing_postal_code=input("Enter billing postal code :")
    total=input("Enter total :")
    ui=Invoices(invoce_id,customer_id,invoce_date,billing_add,billing_city,billing_state,billing_country,billing_postal_code,total)
    ir=Invoice_repo()
    ir.update_invoices(invoce_id,ui)
    view_get_all_invoices()

def view_delete_invoices():
    invoce_id=input("3. Enter invoice iD : ")
    ir=Invoice_repo()
    ir.delete_invoices(invoce_id)
    view_get_all_invoices()

def view_get_all_invoices():
    '''Fetches and display all invoices.'''
    try:
        g_inv=Invoice_repo()
        gai=g_inv.get_all_invoices() 
        if not gai:
            print(f"No invoices found")
        else:
            print(f"invoices data \n-----")
            for li in gai:
                print(f"Invoice ID: {li.invoce_id}, Customer ID:{li.customer_id},Invo_date:{li.invoce_date},  Billing Address:{li.billing_add},Billing city:{ li.billing_city}, Billing State:{li.billing_state}, Billing Country:{li.billing_country}, Billing Postal Code:{li.billing_postal_code}, Total:{li.total}")
    except Exception as e:
        print(f"an error occurred: {e}")




def get_invoices(invoce_id: int):
    """Fetches and displays Invoices ."""
    try:
        Gi=Invoice_repo()
        Gai=Gi.get_invoices(invoce_id)
        if Gai:
            print(f"Invoice ID: {Gai.invoce_id}, Customer ID:{Gai.customer_id},Invo_date:{Gai.invoce_date},  Billing Address:{Gai.billing_add},Billing city:{ Gai.billing_city}, Billing State:{Gai.billing_state}, Billing Country:{Gai.billing_country}, Billing Postal Code:{Gai.billing_postal_code}, Total:{Gai.total}")
        else:
            print(f"No INvoice found with ID { invoce_id: int}.")
    except Exception as e:
        print(f"an error occurred: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("Press 1. for Creat Invoices by ID")
    print("Press 2. for Update Invoices by ID")
    print("Press 3. for Delete Invoices ID")
    print("Press 4. View for all INvoices : ")
    print("Press 5. View Invoice by ID")
    choice = input("Enter your choice:")

    if choice == "1":
        view_create_invoices()
    elif choice == "2":
        view_update_invoices()
    elif choice=="3":
        view_delete_invoices()
    elif choice=="4":
        view_get_all_invoices()
    elif choice=="5":
        try:
            invoce_id = int(input("Enter Invoices ID: "))
            get_invoices(invoce_id)
        except ValueError:
            print("Envalid ID please enter numerical value")
    else:
        print("invalid choise. Please choose an option 1 to 5")

