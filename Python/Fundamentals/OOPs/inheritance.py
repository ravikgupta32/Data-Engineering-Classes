#Inheritance

class company():

    def __init__(self,com_name,country):
        self.com_name = com_name
        self.country = country 
    def company_info(self):
        print(f'Company name is {self.com_name} in {self.country}')

class employee(company):
    def __init__(self, emp_name,com_name,country):
        self.emp_name=emp_name
        company.__init__(self,com_name,country)
        #self.com_name = com_name
    def emp_info(self):
        print(f'Employee Name is {self.emp_name}')
    def company_info_child(self):
        #One type
        #return super().company_info()
        #other way
        company.company_info(self)
emp1=employee('Rahul','AYT','US')

emp1.company_info_child()