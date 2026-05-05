from abc import ABC, abstractmethod

class BaseElement(ABC):
    def __init__ (self, locator):
        self.__locator = locator
        
    def get_locator(self):
        return self.__locator    
        
    @abstractmethod
    def click(self):
        pass
        
    