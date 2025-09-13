class Book:
    def __init__(self,book_id, title,available_copies):
        self.book_id=book_id
        self.tittle=title
        self.available_copies=available_copies
        self.totalBorrowBooks=0

#   dislay the book and the deatils 


    def view_books(self):
        print(f"The Book id is {self.book_id}, the book name is {self.tittle} and Available copy are {self.available_copies}")


# buying a book to home

    def borrow_book(self,num_copies):
        self.copyies=num_copies
        if num_copies<=self.available_copies:
            self.available_copies-=self.copyies
            self.totalBorrowBooks+=self.copyies
            print(f"You borrow the book is {self.totalBorrowBooks} and remaining books are {self.available_copies}") 

        else:
            print(f"The book have only available copyies is {self.available_copies} ")    
         
# ruturning  back the book to library  
#        
    def return_book(self,num_copies):
        self.returnBook=num_copies
        if self.totalBorrowBooks==0:
            print("you did not borrow any books")
            return
        elif(self.returnBook>=self.totalBorrowBooks):
            print(f"You borrow only {self.totalBorrowBooks} so you did not return more books ")
        else:
            self.available_copies+=self.returnBook
            self.totalBorrowBooks-=self.returnBook
            print(f"You return books are {self.returnBook}  and you have {self.totalBorrowBooks}")

class Library:
    def __init__(self):
        self.books=[
            Book(1,"deep copy",50),
            Book(2,"A girl behind the star",50),
            Book(3," The Essential",50),
            Book(4," The Essential",50),
            Book(5," The Essential",50),
        ]

    def displayBook(self):
        for book in self.books:
            book.view_books()


# checking wether the book id  is correct 
    def checkBook(self,bookid):
        self.bookId=bookid
        for book in self.books:
            if book.book_id==self.bookId:
                return book 
        return None
    
allBooks=Library()
        

# main menu 


while True:

    print("1. for the view the book")
    print("2. borrow the book library to home ")
    print("3. return the book to libraray")
    print("4.exit the menu")

    count=input("Enter the options ")
# Enter 1 for  display the books
    if(count=="1"):
        allBooks.displayBook()
# Enter 2 for  borrow the books
    elif (count=="2"):
        try:
            Bookid=int(input("enter the book id "))
            bookfind=allBooks.checkBook(Bookid)

            if not bookfind:
                print("book id is not found ")
                continue
            borrbok=int(input("enter how to much book copy you want "))
            bookfind.borrow_book(borrbok)
            

        except ValueError:
            print("enter the number only") 

    elif (count=="3"):
# Enter 3 for  return the borrow the books        
        try:
            bookId=int(input("Enter the book id "))
            checkbookId=allBooks.checkBook(bookId)

            if not checkbookId:
                print("book id di not find ")

            cancelbook=int(input("enter your return  book "))    
            checkbookId.return_book(cancelbook)

        except:
            print("Enter the number only")
    elif(count=="4"):
        print("you are exiting the main menu")
        break

    else:
        print("Enter the valid number or 1 to 4")    






        