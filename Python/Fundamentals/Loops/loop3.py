tbl_list= ['products','order','customers']

for i in tbl_list:
    print(i)
    if(i.lower()=='order'):
        break
        print(i) #Code unreachable here

print('Second loop')
print('')
print('')
for i in tbl_list:
    if(i.lower()=='order'):
        continue
    print(i)