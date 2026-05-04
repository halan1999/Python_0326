class Phone:
    def __init__(self):
        self.__battery_level = 100  # Thuộc tính private
    def use_app(self, hours):
        for hour in range(1, hours + 1):
            self.__battery_level -= 10  # Giảm mức pin mỗi giờ sử dụng
            if self.__battery_level <= 0:
                self.__battery_level = 0
                break   
            print(f"Giờ thứ {hour}, mức pin hao hụt hiện tại: {self.__battery_level}%")

    def charge_phone(self, hours):
        for hour in range(1, hours + 1):
            self.__battery_level += 20  # Tăng mức pin mỗi giờ sạc
            if self.__battery_level > 100:
                self.__battery_level = 100
                break
            print(f"Giờ thứ {hour}, mức pin đang sạc hiện tại: {self.__battery_level}%")
    def display_battery(self):
        print(f"Mức pin hiện tại: {self.__battery_level}%")
phone = Phone()
phone.use_app(10)
phone.charge_phone(5)
phone.display_battery()