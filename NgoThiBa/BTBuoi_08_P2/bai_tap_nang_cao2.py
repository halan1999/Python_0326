class DriverFactory:
    
    @staticmethod
    def get_driver(broser_name):
        browser_name = browser_name.lower()
        
        if browser_name == "chrome":
            print("Initializing Chrome Driver...")
            return "ChromeDriver object"
        elif browser_name == "firefox":
            print("Initializing Firefox Driver...") 
            return "FirefoxDriver object"
        else:
            raise ValueError("Browser không được hỗ trợ")