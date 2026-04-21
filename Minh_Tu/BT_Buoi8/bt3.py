class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = "Locator của textbox Username"
        self.password_locator = "Locator của textbox password"
        self.login_button_locator = "Locator của login button"
           
    def enter_username(self, username):
        print(f'Tìm element username {self.username_locator}')
        print(f"Nhập username: {username}")
        
    def enter_password(self, password):
        print(f'Tìm element password {self.password_locator}')
        print(f"Nhập username: {password}")
        
    def click_login(self, login_button):
        print(f'Tìm element login button {self.login_button_locator}')
        print('Đã click login button thành công!')
        
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        
page = LoginPage('chrome driver')
page.login('test', '123456')
