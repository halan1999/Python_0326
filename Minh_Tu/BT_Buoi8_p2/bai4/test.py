from momo import MomoPayment
from creditcard import CreditCardPayment


momo1 = MomoPayment()
momo1.process_payment(50000)

credit1 = CreditCardPayment()
credit1.process_payment(100000)
