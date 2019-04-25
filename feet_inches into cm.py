ft = float(input("Enter height in foot: "))
inch = float(input("Enter height in inches (if less than a foot): "))
fttoinch = ft * 12
ftinchtocm = (fttoinch + inch) * 2.5
print ("Foot: ", ft)
print ("Inches: ", inch)
print ("Height in cm: ", ftinchtocm)