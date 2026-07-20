#Parent 1
class company():

    def __init__(self,com_name):
        self.com_name = com_name
    def company_info(self):
        print(f'Company name is {self.com_name}')
    def showme(self):
        print('I am first')
class department(company):
    def __init__(self,dept_name,com_name):
        self.dept_name = dept_name
        company.__init__(self,com_name)
    def department_info(self):
        print(f'The department is {self.dept_name} of {self.com_name}')
    def showme(self):
        print('I am second level')
class employee(department):
    def __init__(self, emp_name,dept_name,com_name):
        self.emp_name =emp_name
        department.__init__(self,dept_name,com_name)

    def all_info(self):
        print(f'The department is {self.dept_name} of {self.com_name}. Employee name is {self.emp_name}')
    
    def showme(self):
        print('I am third level')

emp1=employee('Rahul','HR','ZYX')
emp1.all_info()
emp1.department_info()
emp1.company_info()
emp1.showme()