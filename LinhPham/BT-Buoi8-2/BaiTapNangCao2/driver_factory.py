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
            raise ValueError("Browser không được hỗ trợ")
        

dr1 = DriverFactory.get_driver("chrome")
dr2 = DriverFactory.get_driver("edge")