#Alinkar Lu
#643040818-5

import re

my_info = "My name:Manee DeeJai My ID is 642285829"
search_result = re.split(":", my_info)
name1_str = search_result[1]
name1 = re.search("M.....e", my_info)
name2 = re.search("M..........i+", name1_str)
name3 = re.search("M......s", my_info)
name4 = re.search("\d{9}" ,my_info)


print(f"{name1.group()} is {name2.group()}")
print(f"{name3.group()} {name4.group()}")
