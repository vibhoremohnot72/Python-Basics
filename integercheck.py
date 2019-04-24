x = input("Enter a value: ")
y = input("Enter a value: ")
if not (isinstance(x, int) and isinstance(y, int)):
    raise TypeError("Value is not an integer!!")
else:
    print (x+y)