from payment import PaymentGateway

class MomoPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f'Đang xử lí thanh toán momo số tiền {amount}VNĐ Vui lòng quét mã QR.')
        
