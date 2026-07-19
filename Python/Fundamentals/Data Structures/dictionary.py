#Stores key value pair in python
my_dict = {'x':1,'y':2,'z':'3'}
print(my_dict)
#Change the value by key
my_dict['x']=10
print(my_dict)
#Remove a element
my_dict.pop('z')
print(my_dict)
my_dict = {'x':1,'y':2,'z':'3'}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

#Dict inside a dict
my_dict = {'x':1,'y':2,'z':'3','demo':{'a':1,'b':2,'c':3}}

print(my_dict['demo']['b'])