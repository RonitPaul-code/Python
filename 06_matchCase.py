#CONCEPT OF MATCH CASE !!
# input a day number and print the corresponding day name 
day = int(input("Enter day number : "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

    #default case
    case _:
        print("Invalid")

# NOTE - HERE break statement is not compulsory