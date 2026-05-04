class Document:
    def __init__(self, title):
        self.title = title
    def show_info(self):
        print(f"Document Title: {self.title}")
class Article(Document):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author
    def show_info(self):
        print(f"Article Title: {self.title}, Author: {self.author}")
class Email(Document):
    def __init__(self, title, sender):
        super().__init__(title)
        self.sender = sender
    def show_info(self):
        print(f"Email Title: {self.title}, Sender: {self.sender}")

doc = Document("Python traning")
art = Article("OOP in Python", "Alex")
email = Email("Training Schedule", "Anh Tester")
doc.show_info()
art.show_info()
email.show_info()