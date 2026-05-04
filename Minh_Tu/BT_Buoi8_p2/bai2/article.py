from document import Document

class Article(Document):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author
        
    def show_info(self):
        print(f'Bài báo: {self.title} - Tác giả: {self.author}')    