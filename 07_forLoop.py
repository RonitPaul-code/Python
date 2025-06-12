# print all the numbers from 1 to 10 using range() in loop
for a in range(10): #here a starts from 0 and runs till 100-1
    print(a+1)

print("\n\n")

#print any string using for loop
str = "Ronit"
for a in str:
    print(a)

print("\n\n")

#make the variable name ronit but in the output 'n' should be in uppercase 'U'
str = "ronit"
for ch in str:
    print(ch)

    if(ch == 'n'):#using if inside loop is possible 
        print("N")

print("\n\n")

# print all elements of a list using loop 
lst = ["Red", "Yellow", "Pink", "Blue", "Black"]
for elements in lst:
    print(elements)

print("\n\n")

for k in range(1, 12, 3): #range(<start value>, <stop value>, <step value>)
    print(k)

#here loop starts from 1 and goes untill 11 with an iteration of 3 