from validate import is_str_valid,is_positive_num,book_is_exist,get_next_book_id,is_book_available,change_book_status,return_books_by_author

books = [{ "id": 1,"name": "Harry Potter","author": "J.K. Rowling","year": 1997,"available": True},    {        "id": 2,        "name": "The Hobbit",        "author": "J.R.R. Tolkien",        "year": 1937,        "available": True    },    {        "id": 3,        "name": "Clean Code",        "author": "Robert Martin",        "year": 2008,        "available": False    },    {        "id": 4,        "name": "Atomic Habits",        "author": "James Clear",        "year": 2018,        "available": True    },    {        "id": 5,        "name": "The Pragmatic Programmer",        "author": "David Thomas",        "year": 1999,        "available": False    }]


def display_books():
    if len(books) > 0:
        for book in books:
            print(f'id : {book["id"]},name : {book["name"]},autor:{book["author"]},year: {book["year"]}, isavailable?:{book["available"]}')
            
def search_book():
    try : 
        user_input = input("enter a valide name for book")
        if not is_str_valid(user_input):
            raise ValueError("enter a valid name !")
        maybe_found = [bk for bk in books if user_input.lower()in bk["name"].lower() ]
        if len(maybe_found) > 0 :
            return maybe_found
    except ValueError as e:
        print("wrong str")

def add_book():
    try : 
        new_book_name = input("enter a valide name for new book")
        if not is_str_valid(new_book_name):
                    raise ValueError("enter a valid name !")
        new_book_author = input("enter a valide author for new book")
        if not is_str_valid(new_book_author):
                    raise ValueError("enter a valid author !")
        new_book_year = int(input("enter a valide year for new book"))
        if not is_positive_num(new_book_year):
                            raise ValueError("enter a valid year !")
        if book_is_exist(new_book_name,new_book_author,books):
            raise ValueError("the book already exist !!")
        
        new_id = get_next_book_id(books)
        books.append({"id":new_id, "name" :new_book_name, "author":new_book_author,"year":new_book_year,"available" : True})
        print("book has been added succesfuly.")
    except ValueError as e:
        print("wrong value in input !")

def borrow_book():
    try : 
        book_id = int(input("enter a valide ID for  book to borrow"))
        if not is_positive_num(book_id):
            raise ValueError("enter a valid num !")
        maybe_found = [bk for bk in books if bk["id"] == book_id]
        if len(maybe_found) ==0:
            raise ValueError("book doest exist")
        if is_book_available(maybe_found[0]):
            change_book_status(book_id,books,False)
        else : print("this book is not available")
    except ValueError : 
        print("wrong id or id not exist")
        
        
def return_book():
    try : 
        book_id = int(input("enter a valide ID for  book to return"))
        if not is_positive_num(book_id):
                    raise ValueError("enter a valid ID !")
        maybe_found = [bk for bk in books if bk["id"] == book_id]
        if len(maybe_found) ==0:
            raise ValueError("book doest exist")
        if is_book_available(maybe_found[0]):
            print("this book cant be returned cause its already available")
            return
        change_book_status(book_id,books,True)
    except ValueError:
         print("wrong id or id not exist")
         
def get_available_books():
    available_books = [bk for bk in books if bk["available"] == True]
    if len(available_books) > 0:
        for book in available_books:
             print(f'id : {book["id"]},name : {book["name"]},autor:{book["author"]},year: {book["year"]}')
    else : print("there is not available books")

def get_books_by_author():
    try : 
        book_author = input("enter a valide auth to looking for in books")
        if not is_str_valid(book_author):
            raise ValueError("enter a valide auth to looking for in books !")
        founded_books = return_books_by_author(book_author,books)
        if len(founded_books)> 0:
            print("author : ",book_author)
            for book in founded_books:
                        print(f'id : {book["id"]},name : {book["name"]},year: {book["year"]}, isavailable ? {book["available"]}')
        else : print("there is not book by this author")
    except ValueError:
        print("wrong auth or auth not exist")
        