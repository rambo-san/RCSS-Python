import os
file1=open("Abc.txt","r")
file2=open("Bcd.txt","w")
for i in file1:
    file2.write(i)
file2=open("Bcd.txt","r")
print(file2.read())
file1.close()
file2.close()

