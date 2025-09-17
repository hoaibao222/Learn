import time

n = int(input("Enter number: "))
m = 1

for i in range(1, n+1):
    m *= i

print(f"{n}! = {m}")