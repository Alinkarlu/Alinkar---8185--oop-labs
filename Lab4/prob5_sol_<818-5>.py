'''
Alinkar Lu
643040818-5
'''

import logging
n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))
logging.basicConfig(level=logging.DEBUG,
                    filename='logs-8185.txt',
                    filemode='w',
                    format='%(levelname)s:%(name)s:%(message)s')


result = n1 / n2
print(f"The result is {result}")
#result = n1 / n2
#print(f"The result is {result}")
logging.debug(f'n1 = {n1} ')
logging.debug(f'n2 = {n2} ')