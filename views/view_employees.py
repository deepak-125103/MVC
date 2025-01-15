from models.repos.employee_repos import Emp_repo
from models.employees import Employees

def view_create_employee():
    employee_id=input("1. Enter Employee ID : ")
    fist_name=input("Enter First Name : ")
    last_name=input("Enter Last Name : ")
    title=input("ENter Title : ")
    reports_to=input("ENter Reports to : ")
    birth_date=input("Enter Birth Date : ")
    hire_date=input("Enter Hire Date :")
    address=input("Enter Address : ")
    new_employee=Employees(employee_id,fist_name,last_name,title,reports_to,birth_date,hire_date,address)
    er=Emp_repo()
    er.create_employee(new_employee)
    view_all_employee()

def view_update_employee():
    employee_id=input("2. Enter Employee ID : ")
    fist_name=input("Enter First Name : ")
    last_name=input("Enter Last Name : ")
    title=input("ENter Title : ")
    reports_to=input("ENter Reports to : ")
    birth_date=input("Enter Birth Date : ")
    hire_date=input("Enter Hire Date :")
    address=input("Enter Address : ")
    ue=Employees(employee_id,fist_name,last_name,title,reports_to,birth_date,hire_date,address)
    er=Emp_repo()
    er.update_employee(employee_id,ue)
    view_all_employee()

def view_delete_employee():
    employee_id=input("3. Enter Employee ID")
    der=Emp_repo()
    der.delete_employee(employee_id)
    view_all_employee()

def view_all_employee():
    '''Fetch and display all  employee data'''
    try:
        Gae=Emp_repo()
        em=Gae.get_all_employee()
        if not em:
            print("NO Employee data found")
        else:
            print("Employee data is \n----")
            for li in em:
                print(f"Emp ID: {li.employee_id}, First Name:{ li.fist_name}, Last Name:{li.last_name}, Title:{li.title}, ReportsTo:{ li.reports_to}, Birth Date:{li.birth_date}, Hire Date:{li.hire_date}, Address:{li.address}")
    except Exception as e:
        print(f"An Error Occurred {e}")

def view_employee(Emp_id: int):
    '''Fetch and display employee data with ID'''
    try:
        view_em=Emp_repo()
        ve=view_em.get_employee(Emp_id)
        if ve:
            print(f" Emp. ID: {ve.employee_id}, First Name:{ ve.fist_name}, Last Name:{ve.last_name}, Title:{ve.title}, ReportsTo:{ ve.reports_to}, Birth Date:{ve.birth_date}, Hire Date:{ve.hire_date}, Address:{ve.address}")
        else:
            print(f"NO data found with id {Emp_id}")
    except Exception.error as e:
        print(f"Error occured with {e}")

if __name__=="__main__":
    print("Enter your choice")
    print("Press 1. view Create Employee ID :")
    print("Press 2. Update Employee  ID : ")
    print("Press 3. Delete Employee ID : ")
    print("Press 4. for all Employuee data")
    print("Press 5. for get emplyee with ID")
    choice=input("Enter your choice")
    if choice=="1":
        view_create_employee()
    elif choice=="2":
        view_update_employee()
    elif choice=="3":
        view_delete_employee()
    elif choice=="4":
        view_all_employee()
    elif choice=="5":
        try:
            Emp_id=int(input("Enter employee ID: "))
            view_employee(Emp_id)
        except ValueError:
            print("Envalid ID please enter numerical value")
    else:
        print("invalid choise. Please choose an option 1 to 5")