class Phone:
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
        print(f"Dung lượng pin hiện tại: {self.__battery_level}%")


# Test thử
my_phone = Phone()
my_phone.display_battery()   

my_phone.use_app(3)
my_phone.display_battery()   

my_phone.use_app(8)
my_phone.display_battery()   

my_phone.charge_phone(2)
my_phone.display_battery()   

my_phone.charge_phone(10)
my_phone.display_battery()   