my_list =[1,2,3,4,5,6]

new_list =[]

#Traditional approach
for i in my_list:
    new_list.append(i*i)

print(new_list)

#List compreshension
new_list2=[i*i for i in my_list]
print(new_list2)

#Odd or even and if even then append else not
new_list2=[i*i for i in my_list if(i%2)==0 if(i!=6)]
print(new_list2)