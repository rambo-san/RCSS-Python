count=0
sum=0
for i in range(100,200):
    if(i%7==0):
        count+=1
        sum+=i
print("The count of numbers divisible by 7 is: ",count)
print("The sum of numbers divisible by 7 is: ",sum)