import random
import string

letters1 = string.ascii_lowercase
letters2 = string.ascii_uppercase
digits = string.digits
special_chars = string.punctuation
alphabet = digits + special_chars + letters1 + letters2

pwd_length = 9
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(random.choice(alphabet))

print(f"Random password is {pwd}")