class DriverFactory:
    @staticmethod
    def get_driver(browser_name):
        if browser_name == "chrome":
            print("Initializing Chrome Driver...")
            return "ChromeDriver object"
        elif browser_name == "firefox":
            print("Initializing Firefox Driver...")
            return "FirefoxDriver object"
        else:
            raise ValueError(f"Browser {browser_name} không được hỗ trợ.")

browser1 = DriverFactory.get_driver("chrome")


try:
    browser2 = DriverFactory.get_driver("edge")
except ValueError as e:
    print(e)
