import re

password =  str(input("please enter a passowrd:"))

def check_passowrd_strength(password):
    if len(password) < 8:
        print("Passsword is too short")
        return
    
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit")
        return
    
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter")
        return
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter")
        return
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Password must contain at least one special character")
        return
    
    print("Password is strong")

check_passowrd_strength(password)




