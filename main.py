from pyscript import document

def createacc(event=None):
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    result = document.getElementById("result")

    has_letter = False
    has_number = False

    for c in password: #line 11 to line 15 checks whether they contain both numbers and letters
        if c.isalpha():
            has_letter = True
        elif c.isdigit():
            has_number = True

    if len(username) < 7:   # line 17 to line 24 are the conditions for like username and password like it must not be less than 7 characters long and so on and the else is just if the username and password meets all requirements
        result.innerHTML = f"Add at least {7 - len(username)} more characters to proceed."
    elif len(password) < 10:
        result.innerHTML = f"Add at least {10 - len(password)} more to proceed."
    elif has_letter == False:
        result.innerHTML = "Password must contain at least one letter."
    elif has_number == False:
        result.innerHTML = "Password must contain at least one number."
    else:
        result.innerHTML = "Account created successfully!"