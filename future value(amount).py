principal = float(input("Enter principal rate: "))
rate_of_interest = float(input("Enter rate of interest (in percent per annum): "))
time = float(input("Enter time (in years): "))
interest = (principal * rate_of_interest * time) / 100
print ("Total Interest will be", interest)
amount = principal + interest
print ("Total amount to be paid is", amount)