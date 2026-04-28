class Document:
    def __init__(self, title):
        self.title = title
    def show_info(self):
        print(f"Tiêu đề: {self.title}")
    
class Article(Document):
    def __init__(self,title, author):
        super().__init__(title)
        self.author = author
        
    def show_info(self):
        print(f"Bài báo: {self.title} - Tác giả: {self.author}")
        
class Email(Document):
    def __init__(self, title, sender):
        super().__init__(title)
        self.sender = sender
    def show_info(self):
        print(f"Email: {self.title} - Người gửi: {self.sender}")
        
        
        