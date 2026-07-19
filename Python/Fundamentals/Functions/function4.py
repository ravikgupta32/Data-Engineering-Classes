#Multiple parameters using * and print type we get as tuple
def my_func(*p_x):
    print(p_x,type(p_x))

my_func(20,30,40,50,60,70,80)
 

 #Dictonary function
def new_func(**p_x):
   print(p_x,type(p_x))
   print(p_x.keys())

new_func(x=20,y=30,z=30)

