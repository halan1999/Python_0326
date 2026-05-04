from abc import ABC, abstractmethod
class BaseElement(ABC):
    def __init__(self, locator):
        self.__locator = locator
    def get_locator(self):
        return self.__locator
    @abstractmethod
    def click(self): # đảm bảo tất cả các lớp con đều phải implement phương thức click() để có thể click vào phần tử trên giao diện người dùng
        pass
class Button(BaseElement):
    def click(self):
        print(f"Clicking on a button with locator {self.get_locator()}.") #ko thể dùng self.__locator vì nó là private, phải dùng get_locator() để truy cập
class Checkbox(BaseElement):
    def click(self):
        print(f"Toggling a checkbox with locator {self.get_locator()}.")
    def is_selected(self): #lớp con có thể có thêm các phương thức riêng mà lớp cha không định nghĩa.
        print(f"Checking selection status....")
login_button = Button("xpath=//button[@id='login']")
login_button.click()

checkbox = Checkbox("xpath=//input[@type='checkbox']")
checkbox.click()
checkbox.is_selected()