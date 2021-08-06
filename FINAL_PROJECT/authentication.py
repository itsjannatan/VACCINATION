import json

def login(username, password):
    with open("database.json","r") as f:
        users = json.load(f)
        
    is_valid_login = False
    user=None
    temp_user = users[username]
    if(temp_user != None):
        if(temp_user["password"]==password):
            is_valid_login=True
            user={"username":username,
                  "first_name":temp_user["first_name"],
                  "last_name":temp_user["last_name"]}

    return is_valid_login, user
