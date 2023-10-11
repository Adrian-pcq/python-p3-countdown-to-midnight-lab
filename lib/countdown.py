# your code goes here!

import time

def countdown(value):
    while value >0:
        print(f"{value} SECOND(S)!")
        value-=1
    
    print("HAPPY NEW YEAR!")     

def countdown_with_sleep(value):
    while value >0:
        print(f"{value} SECOND(S)!")
        time.sleep(1)
        value-=1

    print("HAPPY NEW YEAR!")

