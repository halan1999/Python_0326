#Bai2: Inheritance (Tính Kế Thừa)

class Document():
    def __init__(self,title):
        self.title = title
        
    def show_info(self):
        print(f"Tieu de: {self.title}")

class Article(Document):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author
    
    def show_info(self):
        print(f"Bai bao: {self.title} - Tac gia: {self.author}")

class Email(Document):
    def __init__(self, title, sender):
        super().__init__(title)
        self.sender = sender

    def show_info(self):
        print(f"Email: {self.title} - Nguoi gui: {self.sender}")

doc = Document("Tai lieu chung")
art = Article("Hoc Python", "Anh Khoa")
ema = Email("Thong bao hop", "Khoa Nguyen")

doc.show_info()
art.show_info()
ema.show_info()