import os
file=open("Abc.txt","w")
file.write("Hello, i am undert the water.")
file=open("Abc.txt","r")
print(file.read())
file=open("Abc.txt","a")
file.write("\nPlease help me.")
file.close()
os.remove("Abc.txt")
    