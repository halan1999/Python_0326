class Phone:
    def __init__(self):
        self.__batery_level = 100
        
    def use_app(self, hour):
        self.__batery_level -= hour*10
        if self.__batery_level < 0:
            self.__batery_level = 0
            
    def change_phone(self, hourch):
        self.__batery_level = self.__batery_level + (hourch*20)        
        
    def display_batery(self):
        print(f" Pin hien tại là {self.__batery_level}%")
        
p1 = Phone()
p1.use_app(5)
p1.display_batery()
p1.change_phone(1)
p1.display_batery()