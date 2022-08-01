'''
Alinkar Lu
643040818-5
'''

import functools

def sum_odd_numbers():
    lst_str = input("Enter numbers in the list:")
    lst_strs = lst_str.split()
    lst_ints = (int(str) for str in lst_strs)
    print(functools.reduce(lambda a, b: a + b, 
    filter(lambda x:x >= 0 and x % 2 == 1, lst_ints)))


if __name__ == '__main__':
    sum_odd_numbers()