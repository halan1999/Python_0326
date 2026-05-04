from abc import ABC, abstractmethod

# Abstract class
class BaseElement(ABC):
    def __init__(self, locator):
        self.__locator = locator  # private

    def get_locator(self):
        return self.__locator

    @abstractmethod
    def click(self):
        pass

# Button class
class Button(BaseElement):
    def click(self):
        print(f"Clicking on a button with locator {self.get_locator()}")


# Checkbox class
class Checkbox(BaseElement):
    def click(self):
        print(f"Toggling a checkbox with locator {self.get_locator()}")

    def is_selected(self):
        print("Checking selection status...")

        
btn = Button("id=submit-btn")
btn.click()

chk = Checkbox("id=remember-me")
chk.click()
chk.is_selected()