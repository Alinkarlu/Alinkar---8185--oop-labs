'''
Alinkar Lu
643040818-5
'''

string = input("Enter string: ")
list_of_letters = list(string)
print(list_of_letters)
vowels = [each for each in string.upper() if each in "aeiouAEIOU"]
print("the entered string is" ,string, "the result of covert a vowel to uppercase is" ,vowels)