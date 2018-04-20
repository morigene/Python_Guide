class Employee:
    raise_amount = 1.04
    num_of_employee = 0
    def __init__(self,first,last,pay):
        self.fname = first
        self.lname = last
       self.pay   = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_employee += 1

    def fullName(self):
        return self.fname + ' ' +self.lname
    # The same as
    def fullName2(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(self.pay * emp_1.raise_amount)
        return self.pay
emp_1 = Employee('Origene','MUTUYIMANA',5000)
emp_2 = Employee('Donatien','MUREGO', 7000)
#
print(emp_1.fname + " " + emp_1.lname)
# The same as above, simply use method
print(emp_1.fullName())
print(emp_2.fullName2())
# You can do also like this
emp_1.fullName()
print(Employee.fullName(emp_1))
# Learn how to use class variable.

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_1.__dict__)
# This is an example showing me how to use class variable
emp_1.raise_amount = 1.05

print(emp_1.__dict__)

# The second example for number of employee
print ( Employee.num_of_employee)

