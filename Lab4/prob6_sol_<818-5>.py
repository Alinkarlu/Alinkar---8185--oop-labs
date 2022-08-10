def sum_of_list(numbers):
    return sum(numbers)

def average(sum, n):   
    if sum > n:
        return sum / n
    else:
        print(f"The list is empty")

def final_data(data):
    for item in data:
        print("Average:", average(sum_of_list(item), len(item)))
        

list1 = [10, 20, 30, 40, 50]
list2 = [100, 200, 300, 400, 500]
list3 = []
lists = [list1, list2, list3]
final_data(lists)

