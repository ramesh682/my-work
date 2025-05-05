
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        
        super().__init__(name, salary)
        self.department = department

    def show_manager_details(self):
        print(f"Manager Name: {self.name}, Salary: {self.salary}, Department: {self.department}")


manager1 = Manager("Rahul", 80000, "IT")

manager1.show_details()
manager1.show_manager_details()
