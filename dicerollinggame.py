print("WELCOME TO THE Dice rolling game")

n = int(input("entered number n:"))

if n > 6 or n < 1:
    print("hey user please give sufficient value")
    print("End of the code")
else:
    l = [1, 2, 3, 4, 5, 6]
    attempt = 0
    import random

    while attempt < 3:
        p = random.choice(l)
        attempt += 1

        if p == n:
            print("you win")
            break
    else:
        print("you failed you have completed 3 attempt")
        print("please try again")