from abc import ABC, abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class MomoPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Đang xử lý thanh toán Momo số tiền {amount} VND... Vui lòng quét mã QR.")
class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Đang xử lý thanh toán thẻ tín dụng số tiền {amount} VND... Vui lòng nhập thông tin thẻ.")

momo = MomoPayment()
credit_card = CreditCardPayment()   
momo.process_payment(5000000)
credit_card.process_payment(7000000)