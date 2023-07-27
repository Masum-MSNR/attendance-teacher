from repo import *


def doLogin(username, password):
    res = getDb().child("users").child(username).get().val()
    if res is None:
        return {"status": False, "message": "Username not found"}
    if res["password"] != password:
        return {"status": False, "message": "Password is incorrect"}
    else:
        return {"status": True, "message": "Login success"}


def doRegister(username, password, fullname, email):
    model = {
        "username": username,
        "password": password,
        "fullname": fullname,
        "email": email
    }
    res = getDb().child("users").child(username).get().val()
    if res is not None:
        return {"status": False, "message": "Username already exists"}
    else:
        getDb().child("users").child(username).set(model)
        return {"status": True, "message": "Register success"}
