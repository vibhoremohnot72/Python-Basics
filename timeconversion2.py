time = float(input("Enter time (in seconds): "))
day = time // (24 * 3600)
time %= (24 * 3600)
hour = time // 3600
hour %= 3600
minute = time // 60
minute %= 60
seconds = time % 60
print ("d:h:m:s -> %d:%d:%d:%d" % (day, hour, minute, seconds))