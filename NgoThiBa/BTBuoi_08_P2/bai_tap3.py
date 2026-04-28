class MotorbikeDelivery:
    def calculate_fee(self, distance_km):
        return distance_km * 5000
        

class GrabDelivery:
    def calculate_fee(self, distance_km):
        return distance_km * 7000
        
class TruckDelivery:
    def calculate_fee (self, distance_km):
        return distance_km * 20000
        
def get_shipping_cost(delivery_method, distance):
    fee = delivery_method.calculate_fee(distance)
    print(f"Tiền ship của bạn là: {fee} nghìn đồng")