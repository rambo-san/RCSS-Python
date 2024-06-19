a=int(input("Enter the number of units consumed: "))
if(a>600):
    amt=a*1
elif(a>400):
    amt=a*0.8
elif(a>200):
    amt=a*0.65
else:
    amt=a*0.5
if(a>400):
    amt+=amt*0.15
if(amt<100):
    amt=100
print("The total amount is: ",amt)
