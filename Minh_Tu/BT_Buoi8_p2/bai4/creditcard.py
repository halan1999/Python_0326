from payment import PaymentGateway

class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f'Đang xử lí thanh toán thẻ tín dụng số tiền {amount}VNĐ Vui lòng nhập thông tin thẻ.')
        
