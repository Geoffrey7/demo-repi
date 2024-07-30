class Employee:

    
    raies_amount = 1.04
    employee_count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.employee_count += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)  
    
    def employee_details(self):
        return ' FirstName:{} \n LastName: {} \n Email: {} \n pay: {}'.format(self.first, self.last, self.email, self.pay)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raies_amount)


emp1 = Employee('Solomon', 'Grandy', 12000)

Employee.apply_raise(emp1)

print(emp1.employee_details())

print(Employee.employee_count)

                   
   