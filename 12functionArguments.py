def average(a = 6, b = 10):
    print("The average of",a,"and",b," is ",(a+b)/2)

average() #Output - The average of 6 and 10  is  8.0
average(a=12) #Output - The average of 12 and 10  is  11.0
average(b=8) #Output - The average of 6 and 8  is  7.0
average(a=16, b=12) #Output - The average of 16 and 12  is  14.0
average(b=12, a=16) #Output - The average of 16 and 12  is  14.0

#########################################################################

def avg(*numbers):#here when we used '*' operator python interprets 'numbers' as a list
    sum=0
    for i in numbers:
        sum+=i
    x = sum/len(numbers)
    return x

X = avg(12, 542, 65, 551, 512)
print("The average is ",X)

#NOTE - when we use '**' operator python interprets 'numbers' as a list