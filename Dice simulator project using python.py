import random 
min_val = 1
max_val = 6

roll_again = 'yes'

while(roll_again == 'yes'):
    print("rolling the dice...")
    print("the value are : ")

    print(random.randint(min_val,max_val))
    print(random.randint(min_val,max_val))

    roll_again = input("roll the dice again?")