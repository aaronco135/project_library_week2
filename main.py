from manager import  display_books , search_book , add_book,borrow_book,return_book,get_available_books,get_books_by_author
import logging
from validate import is_n_inrange 

logging.basicConfig(level=logging.INFO,                                  
    format="%(asctime)s %(levelname)s %(message)s")


def main():
    press = 1
    while press !=0:
        try : 
          press = int(input("""
    ==========  IBRARY MANAGEMENT  ==========  
    1\.  Display all books  
    2\. Search book by name  
    3\. Add new book
    4\. Borrow a book  
    5\. Return a book  
    6\. Display available books
    7\. Display books by author
    0\. Exit
    Choose option:   
        """))

          if not is_n_inrange(press):
            raise ValueError("enter a number btw 0 to 7")
          if press ==0:
             return False
          elif press == 1:
             display_books()
          elif press ==2:
             books = search_book()
             for book in books:
                  print("name" , book["name"], "id:",book["id"],"author : ",book["author"]  )
          elif press ==3:
              add_book()
          elif press ==4:
             borrow_book()
          elif press ==5:
            return_book()
          elif press ==6:
             get_available_books()
          elif press ==7:
             get_books_by_author()

        except ValueError as e:
            logging.error(f'Enter a positive values  {e}')

main()
