import random, os, time, json
from pathlib import Path
class Book:
    def __init__(self, book_id:int, isbn:str, title:str, author:str, genre:str, year:int, status:str="avialable"):
        self.book_id = book_id
        self.isbn = isbn
        # self.book_id # auto generated like primary key
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.status = status
    
    def __str__(self):
        return f"{self.book_id} {self.title} {self.status}"
    
class User:
    def __init__(self, name:str, user_id:int, borrowed_books:list[Book]):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = borrowed_books
    def __str__(self):
        return f"{self.user_id} {self.name} {self.borrowed_books}"

class IdGenerator:
    def __init__(self, max_id: int = 10000):
        ids = list(range(1, max_id + 1))
        random.shuffle(ids)
        self._ids = iter(ids)

    def next_id(self) -> int:
        return next(self._ids)

class LibraryService:
    def __init__(self, books:list[Book], users:list[User] ):
        self.books = books
        self.users = users
    
    def show_books(self):
        return self.books

    def add_book(self, isbn:str, title:str, author:str, genre:str, year:int):
        gen = IdGenerator()
        new_book = Book(book_id=gen.next_id(), isbn=isbn, title=title, author=author, genre=genre, year=year)
        self.books.append(new_book)

    def get_user(self, user_id:int)->User:
        for user in self.users:
            if user.user_id == user_id:
                return user
        raise ValueError("User not found")
    
    def get_user_name(self, name:str)->User:
        for user in self.users:
            if user.name.lower() == name.lower():
                return user
        raise ValueError("User not found")

    def show_users(self):
        return self.users
    
    def get_book(self, book_id:int)->Book:
        for book in self.books:
            if book.book_id == book_id:
                return book
        raise ValueError("Book not found")

    def borrow_book(self, user_id:int, book_id:int):
        user = self.get_user(user_id=user_id)
        book = self.get_book(book_id=book_id)
        if book.status != "available":
            raise ValueError("Book not found")
        book.status = "borrowed"
        user.borrowed_books.append(book)
    
    def return_book(self, user_id:int, book_id:int):
        user = self.get_user(user_id=user_id)
        book = self.get_book(book_id=book_id)
        if book.status != "borrowed":
            raise ValueError("Book not found")
        book.status = "available"
        user.borrowed_books.remove(book)
    
    def search_book(self, search_string: str):
        for book in self.books:
            found_title = book.title.lower().find(search_string.lower()) 
            found_author = book.author.lower().find(search_string.lower())
            if(found_title > -1 or found_author > -1):
                print(f"{book.book_id}  {book.isbn} {book.title} - {book.status}")

class UIManager:

    def __init__(self, user_action:str="", user:User | None=None, library_service:LibraryService | None=None, isLogin:bool=False):
        self.user_action = user_action
        self.library_service = library_service
        self.user = user
        self.isLogin = isLogin

    def clear_screen(self):
        os.system("clear")

    def ui_template(self, message:str):
        print(f"{message}\n")
    
    def prompt(self):
        self.user_action = input("> ")

    def menu(self):
        self.clear_screen()
        self.banner()
        self.ui_template(f"[1-search | 2-inventory | 3-add | 4-borrow | 5-return | 6-users | 7-logout] \n")
        self.prompt() 
    
    def banner(self):
        if self.isLogin:
            username = f"Welcome {self.user.name}"
        else:
            username = ""
        print(f"\n---- Library Portal ----                                   {username} \n")


    def search(self):
        self.clear_screen() 
        while True: 
            self.ui_template("\n---- Search ----")
            print("[1] Return to menu\n")
            search_string = input(">")
            print("\nSearch results:\n")
            for book in self.library_service.books:
                found_title = book.title.lower().find(search_string.lower()) 
                found_author = book.author.lower().find(search_string.lower())
                if(found_title > -1 or found_author > -1):
                    print(f"{book.book_id}  {book.isbn} {book.title} - {book.status}")

            if search_string.lower() == "1":
                break

    def inventory(self):
        self.clear_screen()
        while True:
            self.ui_template("\n---- Inventory ----")
            print("[1] Return to menu\n")
            for book in self.library_service.show_books():
                print(f"{book.book_id}  {book.isbn} {book.title} - {book.status}") 
            self.prompt()
            if self.user_action == "1":
                break
    def borrow_book(self):
        self.clear_screen()
        self.ui_template("\n---- Borrow ----")
        print("Enter Book Id:")
        self.prompt() 
    
        try:
            self.library_service.borrow_book(int(self.user.user_id), int(self.user_action))
            print(f"Booking successful")
        except ValueError:
            print("Book or User not found")
        
        time.sleep(1)

    def return_book (self):
        self.clear_screen()
        self.ui_template("\n---- Return ----")
        print("Enter Book Id:")
        self.prompt()
        try:
            self.library_service.return_book(int(self.user.user_id), int(self.user_action))
            print("Thank you")
        except ValueError:
            print("Book or User not found")
        time.sleep(1)

    def add_book(self):
        self.ui_template("\n---- Add Book----")

    def show_users(self):
        self.clear_screen()
        self.ui_template("\n---- Users ----")
        for user in self.library_service.show_users():
            print(f"{user.user_id} {user.name}")
            if len(user.borrowed_books) > 0:
                for book in user.borrowed_books:
                    print(f"- {book.book_id} {book.title} {book.status}") 
        time.sleep(2)

    def login(self):
       while True: 
            self.clear_screen()
            self.banner()
            user_name = input("Username: ")
            try: 
                self.user = self.library_service.get_user_name(user_name) 
                self.isLogin = True
                break
            except ValueError:
                print("User not found") 
            time.sleep(1)
    
    def logout(self):
            self.clear_screen()
            print("\nlogout successfully")
            time.sleep(1)
            self.isLogin = False
            self.user = None

    SEARCH = "1"
    INVENTORY = "2"
    BORROW_BOOK = "4"
    ADD_BOOK = "3"
    RETURN_BOOK = "5"
    SHOW_USERS = "6"
    LOGOUT = "7"

    def main(self):
        
        while True:

            if not self.isLogin: 
                self.login()

            self.menu()
            if self.user_action == self.SEARCH:
                self.search()
            elif self.user_action == self.INVENTORY:
                self.inventory()
            elif self.user_action == self.ADD_BOOK:
                self.add_book()
            elif self.user_action == self.BORROW_BOOK:
                self.borrow_book()
            elif self.user_action == self.RETURN_BOOK:
                self.return_book()
            elif self.user_action == self.SHOW_USERS:
                self.show_users()
            elif self.user_action == self.LOGOUT:
                self.logout()
                continue


if __name__ == "__main__":

    user_path = Path("user.json")
    with user_path.open("r") as f:
        raw_users = json.load(f)
        users = [User(**data) for data in raw_users]

    lib_path = Path("libraries.json")
    with lib_path.open("r") as f:
        raw_libraries = json.load(f)
        libraries = [Book(**data) for data in raw_libraries]

        lib_app = LibraryService(books=libraries, users=users)
        ui = UIManager(library_service=lib_app)
        ui.main()

# Todo
# 1 admin page for admin
#   1. admin should be only add book
#   2. admin can I user
# 2 Items Borrowed
#