import numbers


a = float(input("Enter a number: "))
b = float(input("Enter a number: "))

sum = float(a) + float(b)
print("%.0f + %.0f = %.1f" % (a,b,a+b))

print("Writing to file numbers.txt")
with open ("numbers.txt" , "w") as w:
 v = w.write(("%.0f + %.0f = %.1f" % (a,b,a+b)))

print("Reading to file numbers.txt")
with open ("numbers.txt" , "r") as r:
 numbers = r.read()
 
 print(numbers)