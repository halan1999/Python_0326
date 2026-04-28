class Phone:
    def __init__(self):
        self.__battery_level  = 100
    def use_app(self, hours):
        self.__battery_level -=  hours * 10
        
        if self.__battery_level < 0: 
            self.__battery_level = 0
    def charge_phone(self, hours):
        self.__battery_level += hours * 20
        
        if self.__battery_level > 100:
            self.__battery_level = 100
    def display_battery (self):
        print(f"dung lượng hiện tại, {self.__battery_level}%")

# IP14 = Phone()
# IP14.display_battery()

# #So pin sau khi dung 3h
# IP14.use_app(3)
# IP14.display_battery()

# #So phin sau khi dung 2h va sac them 3h
# IP14.use_app(2)
# IP14.charge_phone (3)
# IP14.display_battery()
# #So pin sau khi het va sac them 3h