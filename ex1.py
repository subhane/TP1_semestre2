import random
import string

def randomPassword():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols

    temp = random.sample(all, 8)

    password = "".join(temp)
    return password


def securityLevel(password):
    symbols = []
    if password.islower():
        for i in password:
            if (ord(i)>=21 and ord(i)<=54) or (ord(i)>=91 and ord(i)<=96) or (ord(i)>=123 and ord(i)<=126):
                symbols.append(True)
            else:
                symbols.append(False)
        if True in symbols:
            return("NON VALABLE")
        else:
            return("FAIBLE")
    elif not(password.islower()) and not(password.isupper()):
        for i in password:
            if (ord(i)>=21 and ord(i)<=54) or (ord(i)>=91 and ord(i)<=96) or (ord(i)>=123 and ord(i)<=126):
                symbols.append(True)
            else:
                symbols.append(False)
        if True in symbols:
            return("Fort")
        else:
            return("MOYEN")
    else:
        return("NON VALABLE")


password = randomPassword()
print(password)
print(securityLevel(password))

