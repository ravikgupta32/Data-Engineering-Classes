#Parent 1
class company():

    def __init__(self,com_name):
        self.com_name = com_name
    def company_info(self):
        print(f'Company name is {self.com_name}')
#Parent 2
class country():
    def __init__(self,country_name):
        self.country_name = country_name

    def country_info(self):
        print(f'Country Name us {self.country_name}')
class employee(company,country):
    def __init__(self, emp_name,com_name,country_name):
        self.emp_name=emp_name
        company.__init__(self,com_name)
        country.__init__(self,country_name)
        #self.com_name = com_name
    def emp_info(self):
        print(f'Employee Name is {self.emp_name}')
    def company_info_child(self):
        #One type
        #return super().company_info()
        #other way
        company.company_info(self)
    def full_info(self):
        print(f'The employee {self.emp_name} lives in {self.country_name} and works for {self.com_name}')
emp1=employee('Rahul','AYT','US')

emp1.company_info_child()
emp1.country_info()
emp1.full_info() 