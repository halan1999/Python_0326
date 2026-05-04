class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        # Thuộc tính locator
        self.username_locator = "id=username"
        self.password_locator = "id=password"
        self.login_button_locator = "id=login-button"

    def enter_username(self, username):
        print(f"[LoginPage] Tìm element bằng locator: '{self.username_locator}'")
        print(f"[LoginPage] Nhập username: '{username}'")

    def enter_password(self, password):
        print(f"[LoginPage] Tìm element bằng locator: '{self.password_locator}'")
        print(f"[LoginPage] Nhập password: '{password}'")

    def click_login(self):
        print(f"[LoginPage] Tìm element bằng locator: '{self.login_button_locator}'")
        print("[LoginPage] Click nút Login")

    def login(self, username, password):
        print("\n[LoginPage] === Bắt đầu quy trình đăng nhập ===")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        print("[LoginPage] === Quy trình đăng nhập hoàn tất ===\n")

if __name__ == "__main__":
    mock_driver = object()

    page = LoginPage(driver=mock_driver)
    page.login(username="test_user", password="secret123")