import os.path
filename = (input("Enter file name: "))
fileext = (input("Enter file extension: "))
fullfilename = filename + "." + fileext
print (os.path.isfile(fullfilename))