print("WELCOME TO THE PASSWORD GENERATING GAME")
len_password=int(input("entered length of password:- "))
type_password=input("entered type of password:-").lower()
p=""
alpha="abcdefghijklmnopqrstuvwxyz"
numeric="1234567890"
alphanumeric=alpha+numeric
symbol="&!₹?;^√€¥"
bitwise="^&|~<<>>"
if type_password=="alpha":
    import random
    for i in range(len_password):
        p+=random.choice(alpha)
elif type_password=="numeric":
    import random
    for i in range(len_password):
        p+=random.choice(numeric)
elif type_password=="alphanumeric":
    import random
    for i in range(len_password):
        p+=random.choice(alphanumeric)
elif type_password=="symbol":
    import random
    for i in range(len_password):
        p+=random.choice(symbol)
elif type_password=="bitwise":
    import random
    for i in range(len_password):
        p+=random.choice(bitwise)
else:
    print("User give the wrong type the wrong")
print("THat is your generated password:-",p)
print("END OF THE CODE OF GENERATING CODE")