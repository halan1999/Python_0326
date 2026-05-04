class DriverFactory():
    
    @staticmethod
    def get_driver(browser_name):
        if browser_name.lower() == 'chrome':
            print('Initializing Chrome Driver...')
            return 'ChromeDriver object'
        
        elif browser_name.lower() == 'firefox':
            print('Initializing Firefox Driver...')
            return 'FirefoxDriver object'
        
        else:
            raise ValueError("Browser không được hỗ trợ")