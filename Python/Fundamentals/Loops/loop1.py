mylist =['orders','products','customers']

#for loop
for i in mylist:
    print(i)

tbl_list =['order','products','customers']

for i in tbl_list:
    if(i.lower()=='order'):
        print('Table order')
    elif(i.lower()=='products'):
        print('Table products')
    else:
        print('Other tables')