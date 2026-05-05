#Bai1: Encapsulation (Tính Đóng Gói)

class Phone():
    def __init__(self):
        self.__battery_level = 100

    def use_app(self, hours):
        self.__battery_level -= hours * 10
        if self.__battery_level < 0:
            self.__battery_level = 0

    def charge_phone(self, hours):
        self.__battery_level += hours * 20
        if self.__battery_level > 100:
            self.__battery_level = 100

    def display_battery(self):
        print(f"Battery level: {self.__battery_level}%")

phone = Phone()

phone.display_battery()
phone.use_app(3)
phone.display_battery()
phone.charge_phone(1)
phone.display_battery()