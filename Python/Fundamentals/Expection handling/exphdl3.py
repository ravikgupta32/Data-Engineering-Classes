def my_func(p_x):
    try:
        if(p_x %2 ==0):
            return 1
    except Exception as e:
        return e
    finally:
     print('Hello World')

my_func(4)

    
x= 100

def my_func2():
   print(x)

my_func2()

def my_func2():
   x=5
   print(x)

my_func2()

def my_func2():
   global x
   x=5
   print(x)
my_func2()