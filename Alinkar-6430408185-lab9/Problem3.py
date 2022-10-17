'Alinkar Lu 643040818-5'

import csv

def compute_avg(row):
    sum = 0
    for col in row:
        sum = sum + int(col)
        avg = sum/len(row)
    return avg

def swapPositions(list, i, j):   
    list[i], list[j] = list[j], list[i]
    return list
    
with open("numbers.csv", "w", newline='') as g:
    w = csv.writer(g)
    w.writerows([[2,4,6],[3,7,5],[8,9,7]])

with open("numbers.csv") as f:
    lst_append = []
    rows = csv.reader(f)
    for row in rows:
        rows = csv.reader(f)
        avg = compute_avg(row)
        row.append(avg)    
        i, j = 1, 3
        swap = swapPositions(row, i-1, j-1)
        print(swap)
        lst_append.append([swap])

with open("numbers2.csv", "w", newline='') as h:
    w = csv.writer(h)
    for swp in lst_append:
        w.writerows(swp)



        
