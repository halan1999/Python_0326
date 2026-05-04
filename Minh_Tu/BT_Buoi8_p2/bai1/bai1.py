class Phone():
    def __init__(self):
        self.__battery_level = 100    
    
    def use_app(self, hours):
        # mỗi giờ -10%
        self.__battery_level -= hours * 10
        
        # không cho nhỏ hơn 0
        if self.__battery_level <0:
            self.__battery_level = 0
        
    def charge_phone(self, hours):
        # mỗi giờ +20%
        self.__battery_level += hours * 20
        
        # không cho nhỏ hơn 0
        if self.__battery_level >100:
            self.__battery_level = 100
        
    def display_battery(self):
        print(f'dung lượng pin hiện tại {self.__battery_level}%')
        
        
battery = Phone()
battery.display_battery()

battery.use_app(5)
battery.display_battery()

battery.use_app(4)
battery.display_battery()

battery.use_app(1)
battery.display_battery()

battery.charge_phone(2)
battery.display_battery()

battery.charge_phone(2.5)
battery.display_battery()

battery.charge_phone(0.5)
battery.display_battery()
