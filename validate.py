def is_n_inrange(n):
    list_of_choice = [0,1,2,3,4,5,6,7]
    if n in list_of_choice:
        return True
    return False

def is_str_valid(word):
    if word.strip() == '':
        return False
    return True

def is_positive_num(n):
    return n > 0

def book_is_exist(name,author, books):
    for book in books:
        if book["name"] == name and book["author"] ==author:
            return True
    return False

def get_next_book_id(books):
     books = sorted(books,key=lambda x : x["id"])
     return books[-1]["id"] +1

def is_book_available(book):
    if book["available"] == True:
        return True
    return False

def change_book_status(book_id,books,status):
    if status not in [True,False]:
        raise ValueError("wrong status")
    for bk in books:
             if bk["id"] == book_id:
                    bk["available"] = status
                    print("aailable status has been changed to",status )
                    break

def return_books_by_author(author,books):
    maybe_founded = [bk for bk in books if bk["author"] == author]
    if len(maybe_founded) > 0:
        return maybe_founded
    return []