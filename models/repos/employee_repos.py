from models.employees import Employees
from models.repos.a_employees import A_emp
import sqlite3

class Emp_repo(A_emp):
    def create_employee(self, model: Employees)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f" insert into employees values( {model.employee_id}, '{model.fist_name}','{model.last_name}','{model.title}','{model.reports_to}','{model.birth_date}','{model.hire_date}','{model.address}','{model.city}','{model.state}','{model.country}','{model.Postal_code}','{model.phone}','{model.fax}','{model.email}')")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    
    def update_employee(self, employee_id: int, model: Employees)-> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"update employees set EmployeeId={model.employee_id},FirstName= '{model.fist_name}',LastName='{model.last_name}',Title'{model.title}', ReportsTo'{model.reports_to}', BirthDate'{model.birth_date}',HireDate='{model.hire_date}',Address='{model.address}',city='{model.city}',country='{model.country}',Postal_code='{model.Postal_code}',phone='{model.phone}',fax='{self.fax}',email='{model.email}',state='{model.state}'  where EmployeeId={employee_id}")
        except sqlite3.Error as e:
            print(f"Databse error: {e}")

    def delete_employee(self, employee_id: int, model: Employees):
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"delete from employees where EmployeeId={employee_id}")
        except sqlite3.Error as e:
            print(f"databse error : {e}")

    def get_employee(self, employee_id:int)-> Employees:
        try:
            conn=sqlite3.connect("chinook.db")
            print("Data base is connected successfully")
            cursor=conn.execute("select * from employees WHERE EmployeeId=?",(employee_id,))
            row=cursor.fetchone()
            if row:
                return Employees(employee_id=row[0], fist_name=row[1], last_name=row[2], title=row[3], reports_to=row[4], birth_date=row[5], hire_date=row[6], address=row[7])
            else:
                print(f"No Data base is found with {employee_id}")
        except sqlite3.Error as e:
            print(f"Data base Error as {e}")
        finally:
            conn.close()

    def get_all_employee(self)-> list[Employees]:
        data_list=[]
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor=conn.execute("select * from employees")
                for row in cursor:
                    Get=Employees(employee_id=row[0], fist_name=row[1], last_name=row[2], title=row[3], reports_to=row[4], birth_date=row[5], hire_date=row[6], address=row[7])
                    data_list.append(Get)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list