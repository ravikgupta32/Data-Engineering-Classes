x=10

if(x>10):
    print('Greater than 10')
else:
    print('IDK')

#Create a function for resuability

def my_func():
    if(x>10):
        print('Greater than 10')
    else:
        print('IDK')
x=11
my_func()

#Parameter
def my_func(p_x):
    if(p_x>10):
        print('Greater than 10')
    else:
        print('IDK')
my_func(20)
my_func(30)