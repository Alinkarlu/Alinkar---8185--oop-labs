#Alinkar Lu
#643040818-5
import sys

def fib(n):
    return 1 if n <= 2 else  fib(n-2) + fib(n-1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(fib(int(sys.argv[1])))

