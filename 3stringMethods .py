a = "Ronit"
print(len(a))

print(a.upper()) 
#used to print the strings in uppercase but the original string remains same(immutable)
print(a.lower()) #used to print thr string in lowercase

A = "!!Ronit!!!!!!!!!!" #strips the trailing characters
print(A)
print(A.rstrip("!")) #->output : !!Ronit

print(a.replace("Ronit", "Harry"))#used to replace a specific part of the string or the entire string

B = "Hello my name is Ronit"#used to split the string at a specified instance
print(B.split(" ")) 

Z = "roNit"
print(Z.capitalize()) #Make only the first letters of the string capital and all the other characters are converted into lowrrcase

print(a.center(50)) #used for alignment
print(len(a.center(50)))

a = "abracadabra"
print(a.count("a")) #output - 5
 
a = "Ronit!!!!!"
print(a.endswith("!!!!")) #True
print(a.endswith("!!!!!!")) #False

str1 = "Welcome to the console"
print(str1.endswith("to", 4, 10)) #checks if the string present inside the specified index ends with the specified string

str1 = "My name is Dan"
print(str1.find("D")) #find a specifies character or substring inside a string

