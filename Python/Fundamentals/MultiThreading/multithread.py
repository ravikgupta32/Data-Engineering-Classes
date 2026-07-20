import time
import random

from concurrent.futures import ThreadPoolExecutor
tables =['orders','products','customers','reviews','cancels']
def my_func(p_x):
        wait = random.randint(1,10)
        time.sleep(wait)
        print(f'I am {p_x} I took {wait} seconds' )

#Without multithreading
# for i in tables:
#         my_func(i)

#with multithreading
# with ThreadPoolExecutor(max_workers=len(tables)) as executor:
#         futures = executor.map(my_func,tables)

#With loops
with ThreadPoolExecutor(max_workers=len(tables)) as executor:
       for i in tables:
            future = executor.submit(my_func,i)