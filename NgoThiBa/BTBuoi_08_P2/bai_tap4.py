from abc import ABC, abstractmethod
class PaymentGateway(ABC):  
    @abstractmethod      
    def process_payment(self, amount):
        pass

class MomoPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Đang xử lí thanh toán Momo số tiền {amount}. Vui lòng quét mã QR")
    
class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Đang xử lý thanh toán thẻ tín dụng số tiền {amount}... Vui lòng nhập thông tin thẻ.")
        