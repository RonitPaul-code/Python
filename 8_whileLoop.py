#print from 1 to 5 
i = 1
while(i<=5):
    print(i,end=" ")  #NOTE(imp) - end in default is "\n" but we can set end to any string 
    i+=1 #i++ does not work in python

print("\n\n")

#print from 5 to 1 
i = 5
while(i>=1):
    print(i,end=" ")
    i-=1 #i-- does not work in python

print("\n\n")

#while loop with else
i=1
while(i<=3):
    print(i,end=" ")
    i+=1
else:
    print(" Now I am in ",i)