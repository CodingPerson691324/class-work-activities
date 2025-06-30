class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


book1 = Book('Harry Potter' , 'JKrowling' , 309)
book2 = Book('Tom Sauyer' , 'Mark Twain' , 232)
book3 = Book('The Lord Of The Rings' , 'J.R.R Tolkien' , 1137)

print(book1.title)
print(book1.author)
print(book1.pages)
print(book2.title)
print(book2.author)
print(book2.pages)
print(book3.title)
print(book3.author)
print(book3.pages)