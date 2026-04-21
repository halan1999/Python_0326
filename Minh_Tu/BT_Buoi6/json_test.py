import json

with open('../python/BT_Buoi6/user_data.json', 'r', encoding='utf-8') as data:
    try:
        user_data = json.load(data)
        print(f'username : {user_data['user_name']}')
        print(f'password : {user_data['password']}')
    except json.JSONDecodeError:
        print('Json Error')
    except FileNotFoundError:
        print('File not found')