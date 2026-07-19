from functools import reduce
#Lite weight function
addtion = lambda x,y : x+y
var= addtion(10,20)
print(var)

#Map,filter,reduce
 
my_list=[1,2,3,4,5]

def square(p_x):
    return p_x*p_x

#map
result =list(map(square,my_list))
print(result)

#filter
def square2(p_x):
    if(p_x %2 ==0):
        return p_x*p_x


result = list(filter(square2,my_list))
print(result)

#reduce
def square3(p_x,p_y):
    return p_x+p_y

result =reduce(square3,my_list)
print(result)