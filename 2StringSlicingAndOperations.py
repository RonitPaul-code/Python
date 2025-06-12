names = "Processor"

print(len(names))

print(names[0:5])#here index 5 is not accesed i.e. from 0 to (n-1)
print(names[:5])#[:5] is automatically interpreted as [0:5]
print(names[0:])#[0:] is automatically interpreted as [0:len(names)]

#NEGATIVE SLICING
print(names[0:-3])# [0:-3] = [0, len(names)-3]
print(names[0:len(names)-3])

nm = "Harry"
print(nm[-3:-1])

#loop through strings