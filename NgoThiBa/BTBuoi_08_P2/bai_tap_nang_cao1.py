from abc import ABC, abstractmethod

class BaseElement(ABC):
    def __init__(self, locator):
        self.__locator = locator
    def get_locator(self):
        return self.__locator
    
    @abstractmethod
    def click(self):
        pass
    
class Button(BaseElement):
    def click(self):
        print(f"Clicking on a button with locator {self.__locator}.")
        
class Checkbox (BaseElement):
    def click(self):
        print(f"Toggling a checkbox with locator {self.__locator}.")
        
    def is_selected(self):
        print("Checking selection status....")
    