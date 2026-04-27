class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = "input_username"
        self.password_locator = "input_password"
        self.login_button_locator = "btn_login"

    def enter_username(self, username):
        print(f"Tìm element {self.username_locator} và nhập username: {username}")

    def enter_password(self, password):
        print(f"Tìm element {self.password_locator} và nhập password: {password}")

    def click_login(self):
        print(f"Click vào {self.login_button_locator}")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

driver = "FakeDriver"
login_page = LoginPage(driver)
login_page.login("admin", "123456")