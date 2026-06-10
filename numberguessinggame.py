print("WELCOME TO THE MY NUMBER GUESsINg GAME")
starting=int(input("entered starting:"))
ending=int(input("entered the ending:"))
import random
p=random.randint(starting,ending)
attempt=0
max_attempt=5
while(attempt<max_attempt):
    num=int(input("entered number: "))
    attempt+=1
    if num>p:
        print(" please entered the small value")
    elif num<p:
        print("please entered the big value")
    else:
        print("hi user you guess correct number after {s} attempt".format(s=attempt))
        print(" you win!!!")
        break
else:
    print("you used 5 attempt failed!")
    print("correct number is ",p)
print("END OF THE GAME")