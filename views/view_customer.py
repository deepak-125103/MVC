from models.repos.customer_repo import Customer_repo
from models.customers import Customer

def view_create_album():
    customer_id=input("1. Enter Customer ID : ")
    first_name=input("Enter first name :")
    last_name=input("Enter last name :")
    company=input("Enter company :")
    address=input("Enter address :")
    city=input("Enter city :")
    state=input("Enter state :")
    country=input("Enter country :")
    Postal_code=input("Enter Postal code :")
    phone=input("Enter phone no. :")
    fax=input("Enter fax : ")
    email=input("Enter email :")
    support_repid=input("Enter support rep id :")
    new_customer=Customer(customer_id, first_name, last_name, company, address, city, state, country, Postal_code, phone, fax, email, support_repid)
    cr=Customer_repo()
    cr.create_customer(new_customer)
    view_all_customer()

def view_update_customer():
    customer_id=input("2. Enter Customer ID : ")
    first_name=input("Enter first name :")
    last_name=input("Enter last name :")
    company=input("Enter company :")
    address=input("Enter address :")
    city=input("Enter city :")
    state=input("Enter state :")
    country=input("Enter country :")
    Postal_code=input("Enter Postal code :")
    phone=input("Enter phone no. :")
    fax=input("Enter fax : ")
    email=input("Enter email :")
    support_repid=input("Enter support rep id :")
    uc=Customer(customer_id, first_name, last_name, company, address, city, state, country, Postal_code, phone, fax, email, support_repid)
    cr=Customer_repo()
    cr.update_customer(customer_id,uc)
    view_all_customer()   

def view_delete_customer():
    customer_id=input("3. Enter Customer ID")
    cr=Customer_repo()
    cr.delete_customer(customer_id)
    view_all_customer()

def view_all_customer():
    '''fetch and display all customer'''
    try:
        vac=Customer_repo()
        vc=vac.get_all_customer()
        if not vc:
            print("No customer found")
        else:
            print("customer databse is \n-----")
            for li in vc:
                print(f"ID:{li.customer_id}, First name:{li.first_name}, last name:{li.last_name}, company:{li.company}, address:{li.address}, city:{li.city}, state:{li.state}, country:{li.country}, Postal Code:{li.Postal_code}, Phone:{li.phone}, Fax:{li.fax}, Email:{li.email}, Support:{li.support_repid}")
    except Exception as e:
        print(f"an error occurred: {e}")


def view_customer(customer_id:int):
    '''Fetch and display customer by ID'''
    try:
        vc=Customer_repo()
        
        vci=vc.get_customer(customer_id)
        if vci:
            print(f"ID:{vci.customer_id}, First name:{vci.first_name}, last name:{vci.last_name}, company:{vci.company}, address:{vci.address}, city:{vci.city}, state:{vci.state}, country:{vci.country}, Postal Code:{vci.Postal_code}, Phone:{vci.phone}, Fax:{vci.fax}, Email:{vci.email}, Support:{vci.support_repid}")
        else:
            print(f"No customer type found with ID {customer_id}.")
    except Exception as e:
        print(f"an error occurred: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("Press 1. Create customer : ")
    print("Press 2. Update customer : ")
    print("Press 3. Delete customer : ")
    print("Press 4. View for all customer type ")
    print("Press 5. View customer by ID")
    choice = input("Enter your choice:")

    if choice == "1":
        view_create_album()
    elif choice == "2":
        view_update_customer()
    elif choice=="3":
        view_delete_customer()
    elif choice=="4":
        view_all_customer()
    elif choice=="5":
        try:
            customer_id = int(input("Enter customer type ID: "))
            view_customer(customer_id)
        except ValueError:
            print("Envalid ID please enter numerical value")
    else:
        print("invalid choise. Please choose an option in 1 to 5")

