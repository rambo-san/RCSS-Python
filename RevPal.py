def rev(n):
    r=0
    while(n>0):
        r=r*10+n%10
        n=n//10
    return r
def pal(n):
    if(n==rev(n)):
        return True
    return False
n=int(input("Enter a number: "))
r=rev(n)
print("The reverse of the number is: ",r)
n+=r
print("The sum of the number and its reverse is: ",n)
while(not pal(n)):
    n+=rev(n)
    print("The sum of the new number and its reverse is: ",n)

print("The palindrome number is: ",n)
