class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        username_locator = "username"
        password_locator = "password"
        login_button_locator = "login-button"
    def enter_username(self, username):
        print(f"Nhập tên người dùng: {username}")
    def enter_password(self, password):
        print(f"Nhập mật khẩu: {password}")
    def click_login(self):
        print("Nhấn vào nút đăng nhập")
login = LoginPage("WebDriver")
login.enter_username("user123")
login.enter_password("pass123")
login.click_login()

