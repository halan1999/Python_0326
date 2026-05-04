class MotorbikeDelivery:
    def calculate_fee(self, distance_km):
        return distance_km * 5000


class GrabDelivery:
    def calculate_fee(self, distance_km):
        return distance_km * 7000


class TruckDelivery:
    def calculate_fee(self, distance_km):
        return distance_km * 20000


def get_shipping_cost(delivery_method, distance):
    fee = delivery_method.calculate_fee(distance)
    print(f"Phí giao hàng: {fee:,} VNĐ")


# Test thử
motorbike = MotorbikeDelivery()
grab = GrabDelivery()
truck = TruckDelivery()

print("--- Giao 10km ---")
get_shipping_cost(motorbike, 10)  
get_shipping_cost(grab, 10)        
get_shipping_cost(truck, 10)       