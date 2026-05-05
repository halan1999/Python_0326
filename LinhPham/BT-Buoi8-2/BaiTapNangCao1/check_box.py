from base_element import BaseElement

class CheckBox(BaseElement):
    
    
    def click(self):
        print(f"Toggling a check box with locator {self.get_locator()}")
        
    def is_seleting(self):
        print(f"checking selection stattus...")
        
        
cb1 = CheckBox("chrome")
cb1.click()
cb1.is_seleting()