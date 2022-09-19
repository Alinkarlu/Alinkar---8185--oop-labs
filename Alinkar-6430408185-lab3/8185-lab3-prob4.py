'''
Alinkar Lu
643040818-5
'''

def change_cases(s):
    return str(s).upper()
string = input("Enter string: ")
list_of_letters = list(string)
print(list_of_letters)
vowels = [each for each in string.upper() if each in "aeiouAEIOU"]
result = map(change_cases, vowels) 

print(f"the entered string is" ,string, f"the result of covert a vowel to uppercase is {list(result)}")