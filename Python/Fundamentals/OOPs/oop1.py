class employee():
    emp_name ='Ravi'
    emp_dept ='IT'

    #Below one will give error 
    # def info(self):
    #     print(f'Employee {emp_name} works for {emp_dept}')
    #Correct one
    # def info(self):
    #     print(f'Employee {self.emp_name} works for {self.emp_dept}')
    #One which expects parameters
    def info(self,emp_name,emp_dept):
        print(f'Employee {emp_name} works for {emp_dept}')


emp1 = employee()
print(emp1.emp_name)
emp1.info('Ravi','Software')

#emp1.info() is equivalent to employee.info(emp1)
