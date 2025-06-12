#Write a python program that can greet you with good morning, good afternoon and 
#good night according to the current hour
#HINT - USE time MODULE
import time

# Get the current hour as an integer
current_hour = int(time.strftime('%H'))

if 5 <= current_hour < 12:
    print("GOOD MORNING")
elif 12 <= current_hour < 17:
    print("GOOD AFTERNOON")
elif 17 <= current_hour < 21:
    print("GOOD EVENING")
else:
    print("GOOD NIGHT")
