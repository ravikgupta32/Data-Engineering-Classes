#Getter and Setter
class employee():
    company_name ='XYZ'
    def __init__(self,emp_name,emp_dept): #This is a constructor
        self.emp_name =emp_name
        self.emp_dept =emp_dept

    @property #Getter
    def info(self):
        print(f'Employee {self.emp_name} works for {self.emp_dept} in {self.company_name}')

    @info.setter #Setter
    def info(self,new_empdetails):
            new_empname = new_empdetails[0]
            new_emptdept = new_empdetails[1]
            self.emp_name=new_empname
            self.emp_dept=new_emptdept

    def changeinfo(self,new_empname,new_emptdept):
        self.emp_name= new_empname
        self.emp_dept=new_emptdept
 
    #Alternative to Class Method
    def changes(self,new_company):
        employee.company_name=new_company
    #Static method in python is below
    @staticmethod
    def addition(x,y):
        print(x+y)

    #Class method
    @classmethod
    def changesInClass(cls,new_company):
        cls.company_name = new_company #Class attribute is cls

emp1=employee('Ravi','IT')
print(emp1.info)

emp1.info=['Ravinder','HR']
print(emp1.info)

