from document import Document

class Article(Document):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author
        
    def show_info(self):
        print (f"Bai bao {self.title} - Tac gia {self.author}")
        
articel1 = Article("Môi trường sống", "Nguyen Van A")
articel1.show_info()