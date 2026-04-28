class LoginPage:
    def __init__(self, username: str, password:str, login_button):
        self.username_locator = username
        self.password_locator = password
        self.login_button_locator= login_button

def enter_username(self, username):
    print(f" Element là {self.username}")
    print (f"Nhập username là: {username}")
    
def enter_password (self, password):
    print (f"Emlement là {self.password}")
    print(f"Nhập password: {password}")
    
def click_login(self):
    print(f"Element là {self.login.button}")
    print("Click on Login button")
    
def login(self, username, password):
    self.username(username)
    self.password(password)
    self.login_button()

