from repo import *


def doLogin(username, password):
    res = getDb().child("users").child(username).get().val()
    if res is None:
        return {"status": False, "message": "Username not found"}
    if res["password"] != password:
        return {"status": False, "message": "Password is incorrect"}
    else:
        return {"status": True, "message": "Login success", "data": res}


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


def doCreateClass(class_name, class_code, username):
    res = getDb().child("users").child(username).get().val()
    model = {
        "username": username,
        "class_name": class_name,
        "class_code": class_code,
        "fullname": res["fullname"],
    }
    res = getDb().child("classes").child(class_code).get().val()
    if res is not None:
        return {"status": False, "message": "Class code already exists"}
    else:
        getDb().child("classes").child(class_code).set(model)
        return {"status": True, "message": "Create class success"}


def getClassesByUsername(username):
    res = getDb().child("classes").order_by_child("username").equal_to(username).get().val()
    if res is None:
        return {"status": False, "message": "Class not found"}
    else:
        return {"status": True, "data": res}


def getClassByCode(class_code):
    res = getDb().child("classes").child(class_code).get().val()
    if res is None:
        return {"status": False, "message": "Class not found"}
    else:
        return {"status": True, "data": res}
