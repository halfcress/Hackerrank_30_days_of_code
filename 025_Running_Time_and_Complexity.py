"""import sympy

n = input()
n = int(n)
l = []

for _ in range(n):
    l.append(int(input()))

for i in l:
    x = sympy.isprime(i)
    if x:
        print("Prime")
    else:
        print("Not prime")"""  # Best solution. But hackerrank not support sympy library.


for _ in range(int(input())): #Without library.
    num = int(input())
    if (num == 1):
        print("Not prime")
    else:
        if (num % 2 == 0 and num > 2):
            print("Not prime")
        else:
            for i in range(3, int(num ** (1 / 2)) + 1, 2):
                if num % i == 0:
                    print("Not prime")
                    break
            else:
                print("Prime")
