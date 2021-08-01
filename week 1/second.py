class employee():
    def __init__(self, name, age, id, salary): # creating a function
        self.name = name # self is an instance of a class
        self.age = age
        self.salary = salary
        self.id = id

    def show_employee(self):
        print('Employee Name ', self.name, ' Age ',
            self.age, ' Salary ', self.salary, ' ID: ', self.id)


emp1 = employee("Peter", 22, 1000, 1234) # creating objects
print(emp1.__dict__) # Prints dictionary
emp2 = employee("Bob", 23, 2000, 2234)
emp2.show_employee()