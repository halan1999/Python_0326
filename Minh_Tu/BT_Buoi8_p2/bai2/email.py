from document import Document

class Email(Document):
    def __init__(self, title, sender):
        super().__init__(title)
        self.sender = sender
        
    def show_info(self):
        print(f'Email: {self.title} - Người gửi: {self.sender}')    