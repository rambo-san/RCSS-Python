def choice():
    print("Menu:\n1 - Check substring\n2 - Count occurance\n3 - Replace substring\n4 - Convert to Capital Letters\n5 - Exit\nEnter your choice: ")
    ch=int(input())
    return ch

s=input("Enter the string: ")
while(True):
    ch=choice()
    if(ch==1):
        sub=input("Enter the substring to be checked: ")
        if(sub in s):
            print("The substring is present in the string")
        else:
            print("The substring is not present in the string")
    elif(ch==2):
        sub=input("Enter the substring to be counted: ")
        print("The substring occurs",s.count(sub),"times in the string")
    elif(ch==3):
        sub=input("Enter the substring to be replaced: ")
        rep=input("Enter the substring to replace: ")
        s=s.replace(sub,rep)
        print("The new string is: ",s)
    elif(ch==4):
        print("The string in capital letters is: ",s.upper())
    else:
        break