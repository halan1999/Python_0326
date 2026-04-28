import json

with open("../BT_Buoi6/data.json", "r", encoding="utf-8") as f:
    try:
        user_data = json.load(f)
        print(f"Username: {user_data["username"]}")
        print(f"email: {user_data["email"]}")
        print(f"password: {user_data["password"]}")
    
    except  json.JSONDecodeError:
        print("Json is invalid")
    except FileNotFoundError:
        print("File is not exsiting")
            
        