class employee():
    company_name ='XYZ'
    def __init__(self,emp_name,emp_dept): #This is a constructor
        self.emp_name =emp_name
        self.emp_dept =emp_dept
    def info(self):
        print(f'Employee {self.emp_name} works for {self.emp_dept} in {self.company_name}')

emp1=employee('Henry','BPO')
emp1.info()
emp2 = employee('Ravi','IT')
emp2.info()

emp2.company_name='ABC'
print(emp2.company_name)
print(emp1.company_name)

employee.company_name ='ABC'

emp1.info()