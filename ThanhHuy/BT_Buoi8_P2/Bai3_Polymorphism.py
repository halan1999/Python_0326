class MotobikeDelivery:
    def __init__(self):
        pass
    def calculate_fee(self, distance_km):
        return distance_km * 5000
class GrabDelivery:
    def __init__(self):
        pass
    def calculate_fee(self, distance_km):
        return distance_km * 7000
class TruckDelivery:
    def __init__(self):
        pass
    def calculate_fee(self, distance_km):
        return distance_km * 20000
def get_shipping_cost(delivery_method, distance_km):
    return delivery_method.caculate_fee(distance_km)
motobike = MotobikeDelivery()
grab = GrabDelivery()
truck = TruckDelivery()
distance = 10
print(f"Phí vận chuyển bằng xe máy: {get_shipping_cost(motobike, distance)} VND")
print(f"Phí vận chuyển bằng Grab: {get_shipping_cost(grab, distance)} VND")
print(f"Phí vận chuyển bằng xe tải: {get_shipping_cost(truck, distance)} VND")
