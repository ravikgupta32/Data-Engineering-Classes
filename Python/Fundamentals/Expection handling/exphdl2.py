x= "10"

try:
    if (x>10):
        print('Greater than 10')
    else:
        print('Else')
except Exception as e:
    print(f' Hey you got this error -{e}')

finally:
    print('I will always run')
print('Hello World')