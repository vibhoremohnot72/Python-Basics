from math import gcd
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
lcm = (a * b) // gcd(a,b)
print (lcm)