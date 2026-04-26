class LoginPage:
    def __init__(self, driver : str):
        self.driver = driver
        self.username_locator = "#username"
        self.password_locator = "#password"
        self.login_button_locator = "#login"

    #nhập thông tin
    def enter_username(self, username : str):
        print("Tìm ô user name: ", self.username_locator)
        print("Nhập user name: ", username)

    def enter_password(self, password : str):
        print("Tìm ô password: ", self.password_locator)
        print("Nhập pass word: ", password)

    def click_login(self):
        print("Tìm nút login", self.login_button_locator)
        print("Click nút login - Login thành công")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


driver = "Chrome"
user1 = LoginPage(driver)

user1.login("Admin", "123456")