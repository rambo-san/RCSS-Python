print("enter Operand 1 :")
op1=int(input())
print("enter Operand 2 :")
op2=int(input())
print("Select Opearator")
opr=input()
if(opr=='+'):
    print(op1+op2)
elif(opr=='*'):
    print(op1*op2)
elif(opr=='/'):
    print(op1/op2)
elif(opr=='-'):
    print(op1-op2)
elif(opr=='%'):
    print(op1%op2)
else:
    print("Enter a valid Operator")