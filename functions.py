def password_check(password):
    caps = False
    nums = False
    lows = False
    for i in password:
        if i.isupper() == True:
            caps = True
        elif i.islower() == True:
            lows = True
        elif i.isdigit() == True:
            nums = True
    if caps == False:
        print("ERROR: CAPITALS NEEDED")
    if lows == False: 
        print("ERROR: LOWERCASE NEEDED")
    if nums == False:
        print("ERROR: NUMBERS NEEDED")
    if len(password) <= 8:
        print("ERROR: PASSWORD MUST BE ATLEAST 8 DIGITS")
    if caps == True and lows == True and nums == True and len(password) >= 8:
        print("PASSWORD ACCEPTED")

password = input("ENTER PASSWORD: ")
password_check(password)