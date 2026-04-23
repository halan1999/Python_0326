class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locater = "#username"
        self.password_locator = "#password"
        self.login_button_locator = "#loginbnb"

        def enter_username(self, username):
            print(f"Tìm ô username: {self.username_locator}")
            print(f"Gõ vào: {username}")

        def enter_password(self, password):
            print(f"Tìm ô password: {self.password_locator}")
            print(f"Gõ vào: {password}")

        def click_login(self):
            print(f"Click nút login: {self.login_button_locator}")

        def login(self, username, password):
            self.enter_username(username)
            self.enter_password(password)
            self.click_login()

        driver = None
        page = LoginPage(driver)
        page.login("admin", "123456")