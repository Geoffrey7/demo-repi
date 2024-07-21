class Employee:
  def __init__(self,first,last,pay) -> None:
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + "." + last + "@gmail.com"

  def fullname(self):
    return '{} {}' .format(self.first, self.last)

emp1 = Employee("Geoffrey", "Kioi","170,000")
emp2 = Employee("Ann","Bell","170,000")

emp1.fullname()
print(Employee.fullname(emp2))

