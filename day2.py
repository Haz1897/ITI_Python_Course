import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234",
    database="employee_system"
)

class Employee:
    employees=[]
    def __init__(self,fn,ln,a,d,s,insert=True):
        self.id=-1
        self.first_name=fn
        self.last_name=ln
        self.age=a
        self.department = d
        self.salary = s
        cursor=connection.cursor()
        if(insert): # To insert when first creating employees, disabled when fetching.
            cursor.execute(f"INSERT INTO employees (First_Name, Last_Name, Age, Department, Salary,Managed_Department) VALUES ('{fn}', '{ln}', {a}, '{d}', {s},'')")
            connection.commit()
        cursor.execute("SELECT ID FROM employees ORDER BY id DESC LIMIT 1")
        emp=cursor.fetchone()
        cursor.close()
        self.id=emp[0]
        Employee.employees.append(self)
    def transfer(self,new_department):
        self.department=new_department
        cursor=connection.cursor()
        cursor.execute(f"UPDATE employees SET Department=\"{new_department}\" WHERE ID=\"{self.id}\" ")
        connection.commit()
        cursor.close()
    def fire(self):
        cursor=connection.cursor()
        cursor.execute(f"DELETE FROM employees WHERE ID=\"{self.id}\" ")
        connection.commit()
        cursor.close()
    def show(self):
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\nAge: {self.age}\nDepartment: {self.department}\nSalary: {self.salary}\n---------------------")
    @classmethod
    def list_employees(cls):
        for emp in cls.employees:
            emp.show()
    @classmethod
    def fetch_all_from_db(cls):
        cls.employees.clear()
        cursor = connection.cursor()
        cursor.execute("SELECT First_Name, Last_Name, Age, Department, Salary, Managed_Department FROM employees")
        rows = cursor.fetchall()
        cursor.close()
        for row in rows:
            if row[5] is None or row[5] == "":
                Employee(row[0], row[1], row[2], row[3], row[4], insert=False)
            else:
                Manager(row[0], row[1], row[2], row[3], row[4], row[5], insert=False)
    
class Manager(Employee):
    def __init__(self,fn,ln,a,d,s,md,insert=False):
        super().__init__(fn,ln,a,d,s,insert)
        self.managed_department=md
        cursor=connection.cursor()
        cursor.execute(f"UPDATE employees SET Managed_Department=\"{md}\" WHERE ID=\"{self.id}\"")
        connection.commit()
        cursor.close()
    def show(self):
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\nAge: {self.age}\nDepartment: {self.department}\nSalary: Confidential\n---------------------")


not_done=True
Employee.fetch_all_from_db()
while not_done:
    print("What would you like to do?")
    choice = input(f"Type \"add\" to add a new employee.\nType \"transfer\" to transfer an employee to another department.\nType \"fire\" to fire an employee.\nType \"show\" to show an employee's information.\nType \"show all\" to show data of all employees.\nType \"q\" to exit.\n")
    choice=choice.lower()
    print()
    match choice:
        case "add":
            emp_type = input("Do you want to add an employee or a manager? (e/m): ").lower().strip()
            if emp_type in ["e", "m"]:
                emp_data = [
                    input("Enter first name: ").strip(),
                    input("Enter last name: ").strip(),
                    int(input("Enter age: ")),
                    input("Enter department: ").strip(),
                    float(input("Enter salary: "))
                ]
                if emp_type == "m":
                    managed_department = input("Enter the department they manage: ").strip()
                    emp_data.append(managed_department)
                    Manager(*emp_data)
                    print("Added successfully!\n")
                else:
                    Employee(*emp_data)
                    print("Added successfully!\n")
            else:
                print("Error: Invalid type selection. Please enter 'e' or 'm'.\n")
        case "transfer":
            if not Employee.employees:
                print("Error: No employees available to transfer.\n")
            else:
                for index, emp in enumerate(Employee.employees, 1):
                    print(f"{index}) {emp.first_name} {emp.last_name}")
                
                selection_input = input("Choose employee number: ").strip()
                
                if selection_input.isdigit():
                    selection = int(selection_input)
                    if 1 <= selection <= len(Employee.employees):
                        new_department = input("Enter new department: ")
                        Employee.employees[selection - 1].transfer(new_department)
                        print("Transferred successfully!\n")
                    else:
                        print("Error: Invalid employee number selector.\n")
                else:
                    print("Error: Please input a valid numeric entry choice only.\n")
            
        case "fire":
            if not Employee.employees:
                print("Error: No employees available to fire.\n")
            else:
                for index, emp in enumerate(Employee.employees, 1):
                    print(f"{index}) {emp.first_name} {emp.last_name}")
                
                selection_input = input("Choose employee number: ").strip()
                
                if selection_input.isdigit():
                    selection = int(selection_input)
                    if 1 <= selection <= len(Employee.employees):
                        Employee.employees[selection - 1].fire()
                    else:
                        print("Error: Invalid employee number selector.\n")
                else:
                    print("Error: Please input a valid numeric entry choice only.\n")
            
        case "show":
            if not Employee.employees:
                print("Error: No employees available to show.\n")
            else:
                for index, emp in enumerate(Employee.employees, 1):
                    print(f"{index}) {emp.first_name} {emp.last_name}")
                
                selection_input = input("Choose employee number: ").strip()
                
                if selection_input.isdigit():
                    selection = int(selection_input)
                    if 1 <= selection <= len(Employee.employees):
                        Employee.employees[selection - 1].show()
                        print()
                    else:
                        print("Error: Invalid employee number selector.\n")
                else:
                    print("Error: Please input a valid numeric entry choice only.\n")
            
        case "show all":
            if not Employee.employees:
                print("Error: No employees available to show.\n")
            else:
                Employee.list_employees()
                print()
            
        case "q":
            not_done = False
            print("\nGood bye!")
        