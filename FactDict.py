def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)
dict1={}
n1=int(input("Enter a number: "))
f1=fact(n1)
print("The factorial of the number is: ",f1)
dict1[n1]=f1
n1=int(input("Enter a number: "))
f1=fact(n1)
print("The factorial of the number is: ",f1)
dict1[n1]=f1
n1=int(input("Enter a number: "))
f1=fact(n1)
print("The factorial of the number is: ",f1)
dict1[n1]=f1
n1=int(input("Enter a number: "))
f1=fact(n1)
print("The factorial of the number is: ",f1)
dict1[n1]=f1
print(dict1)