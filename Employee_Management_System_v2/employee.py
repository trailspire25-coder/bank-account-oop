class Employee:
    def __init__(self, ID, name, department, salary):
            
            if not isinstance(ID, int):
                raise ValueError("ID must be number.")
    
            if ID < 0:
                raise ValueError("ID cannot be negative.")
            
            if not isinstance(salary, (int, float)):
                raise ValueError("Salary must be number.")
    
            if salary < 0:
                raise ValueError("Salary cannot be negative.")
    
            if not isinstance(name, str):
                raise ValueError("Name must be text.")
            
            if name.strip().isdigit():
                raise ValueError("Name cannot be a number.")
            
            if not isinstance(department, str):
                raise ValueError("Department must be text.")

            if department.strip().isdigit():
                raise ValueError("Department cannot be a number.")
            
            self.ID = ID
            self.name = name
            self.department = department
            self.salary = salary

    def display_info(self):
         print(f"Employee ID: {self.ID} - "
               f"Employees name: {self.name} - "
               f"Employee department: {self.department} - " 
               f"Employee salary: {self.salary}")

    def update_info(self, new_ID, new_name, new_department, new_salary):
        if not isinstance(new_ID, int):
            raise ValueError("ID must be number.")
            
        if new_ID < 0:
            raise ValueError("ID cannot be negative.")

        if not isinstance(new_salary, (int, float)):
            raise ValueError("Salary must be number.")
                
        if new_salary < 0:
            raise ValueError("Salary cannot be negative.")
            
        if not isinstance(new_name, str):
            raise ValueError("Name must be text.")
                    
        if new_name.strip().isdigit():
            raise ValueError("Name cannot be a number.")
                    
        if not isinstance(new_department, str):
            raise ValueError("Department must be text.")
        
        if new_department.strip().isdigit():
            raise ValueError("Department cannot be a number.")
        
        self.ID = new_ID
        self.name = new_name
        self.department = new_department
        self.salary = new_salary
