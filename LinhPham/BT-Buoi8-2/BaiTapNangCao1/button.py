from base_element import BaseElement

class Button(BaseElement):
    def click(self):
        print(f"Click on the button with the locator {self.get_locator()}")
        
btn1 = Button("#button_locator")
btn1.click()