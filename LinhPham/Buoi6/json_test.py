# Cách mở và đọc file json

import json


with open("../Buoi6/user_data.json", "r", encoding='utf-8') as readfile:
    try:
        user_data = json.load(readfile)
        print(f"user name: {user_data["username"]}")
        print(f"mail: {user_data["emails"]}")
        print(f"pass: {user_data["password"]}")
    except json.JSONDecodeError:
        print("Json error")
    except FileNotFoundError:
        print("file not found")