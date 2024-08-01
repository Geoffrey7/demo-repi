class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self. first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{first} {last}'
    
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Ann', 'Njoki', 120000)
emp2 = Employee('Terry','Wanja', 120000)   

emp1.apply_raise()
print(emp1.pay)


print(Employee.raise_amount)

print(Employee.num_of_emps)
