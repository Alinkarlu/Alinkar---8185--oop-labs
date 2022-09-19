numbers = [1, 2, 3, 4, 5]
print("Before adding an integer, the list is" ,numbers)

def add_number_to_list():
  integer = int(input("Enter a number to add to a list: "))
  numbers.append(integer)
  print("After adding an integer" ,integer, "the list is" ,numbers)

def replace_number_in_list():
  find = int(input("Enter a number to find: "))
  replace = int(input("Enter a number to replace: "))
  
  newlist = [x if x != find else replace for x in numbers]
  print("After replacing" ,replace, "with" ,find, "the list is" ,newlist)

def remove_number_in_list():
  print("Finding a number to remove in the list" ,numbers)
  remove = int(input("Enter a number to remove: "))
  numbers.remove(remove)
  print("After removing" ,remove, "the List is" ,numbers)

if __name__ == '__main__':
    add_number_to_list()
    replace_number_in_list()
    remove_number_in_list()

# Name = Alinkar Lu
# Student ID = 643040818-5