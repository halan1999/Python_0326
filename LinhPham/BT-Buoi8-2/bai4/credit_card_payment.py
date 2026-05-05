from payment_gateway import PaymentGateway

class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Đang xữ lý thẻ tín dụng số tiền {amount}, vui lòng nhập thẻ")
        
c1 = CreditCardPayment()
c1.process_payment(200)