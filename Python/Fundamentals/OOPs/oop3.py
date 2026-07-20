class employee():
    company_name ='XYZ'
    def __init__(self,emp_name,emp_dept): #This is a constructor
        self.emp_name =emp_name
        self.emp_dept =emp_dept
    
    #Alternative to Class
    def changes(self,new_company):
        employee.company_name=new_company
    def info(self):
        print(f'Employee {self.emp_name} works for {self.emp_dept} in {self.company_name}')
    #Static method in python is below
    @staticmethod
    def addition(x,y):
        print(x+y)

    #Class method
    @classmethod
    def changesInClass(cls,new_company):
        cls.company_name = new_company #Class attribute is cls

emp1=employee('Ravi','IT')
emp2 =employee('Henry','HR')
emp1.changesInClass('NewNewCompany')
print(emp1.company_name)
emp1.addition(1,2)

