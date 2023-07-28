def loginValidator(username, password):
    if username == "" or len(username) < 5:
        return {"status": False, "message": "Username must be at least 5 characters"}
    if password == "" or len(password) < 8:
        return {"status": False, "message": "Password must be at least 8 characters"}
    return {"status": True, "message": "Login success"}


def registerValidator(username, fullname, email, password, confirmPass):
    if username == "" or len(username) < 5:
        return {"status": False, "message": "Username must be at least 5 characters"}
    if fullname == "" or len(fullname) < 5:
        return {"status": False, "message": "Fullname must be at least 5 characters"}
    if email == "" or len(email) < 5:
        return {"status": False, "message": "Email must be at least 5 characters"}
    if password == "" or len(password) < 8:
        return {"status": False, "message": "Password must be at least 8 characters"}
    if confirmPass == "" or len(confirmPass) < 8:
        return {"status": False, "message": "Confirm password must be at least 8 characters"}
    if confirmPass != password:
        return {"status": False, "message": "Confirm password must be the same as password"}
    return {"status": True, "message": "Register success"}


def createClassValidator(classname):
    if classname == "":
        return {"status": False, "message": "Classname must not be empty"}
    return {"status": True, "message": "Create class success"}
