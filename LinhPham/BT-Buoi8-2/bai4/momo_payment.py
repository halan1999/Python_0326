from payment_gateway import PaymentGateway

class MomoPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Đang xữ lý thanh toán momo số tiền {amount}, vui lòng quét mã")
        
        
m1 = MomoPayment()
m1.process_payment(100)
