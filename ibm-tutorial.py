class Employee:
    #class attributes
    status = "active"
    number_of_employee = 0

    def __init__(self, employee_id, name):
        self.employee_id = employee_id #instance attribute
        self.name = name #instance attribute
        Employee.number_of_employee += 1

    #instance method
    def give_info(self):
        print("Name: ", self.name, "\nID: ", self.employee_id)

emre = Employee("101", "Emre Kutlug")
print(type(emre))
emre.give_info()


