x='RaviGupta' #Array of characters

print(x[0])
#First 4 character
print(x[0:4])
#Last 4 character 
print(x[4:])
#No of elements in a string array
print(len(x))
print(x[4:len(x)])

#String methods
x='Hello World'
print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.replace('H','z').capitalize())

letter='A new random keyword'
my_list = letter.split(" ")
print(my_list)
file_name = 'raw_data.csv'
if (file_name.endswith('.csv')):
    print('CSV File')

if(file_name.startswith('raw')):
    print('Raw File')
statement ="Hello User. What are you doing. Hey User I am talking to you."

print(statement.count('User'))

#is functions()

demo_str='Hello'
demo_var ="10abc"
print(demo_str.isnumeric())
print(demo_var.isalnum())