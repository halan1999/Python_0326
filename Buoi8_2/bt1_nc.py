from abc import ABC, abstractmethod

class BaseElement(ABC):
    def __init__(self, locator):
        self.__locator = locator  # private

    def get_locator(self):
        return self.__locator

    @abstractmethod
    def click(self):
        pass


class Button(BaseElement):
    def click(self):
        print(f"Clicking on a button with locator {self.get_locator()}")


class Checkbox(BaseElement):
    def click(self):
        print(f"Toggling a checkbox with locator {self.get_locator()}")

    def is_selected(self):
        print("Checking selection status....")


# Test thử
btn = Button("#submit-btn")
btn.click()
print(f"Locator: {btn.get_locator()}")

chk = Checkbox("#agree-checkbox")
chk.click()
chk.is_selected()