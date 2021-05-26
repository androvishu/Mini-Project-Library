import time


class Library:
    def __init__(self, list, Library_name):
        self.Book_list = list
        self.name = Library_name
        self.lend_dict = {}

    def display_book(self):
        print("Available book list is given below: ")
        for i, book in enumerate(self.Book_list):
            time.sleep(1)
            print(f"{i + 1}.{book}")

    def lend_book(self, book, user):
        if book not in self.lend_dict.keys():
            self.lend_dict.update({book: user})
            time.sleep(3)
            print("Lend Book is successfully.")

        else:
            time.sleep(1)
            print(f"Book is already lending by {self.lend_dict[book]}")

    def add_book(self, book):
        self.Book_list.append(book)
        time.sleep(3)
        print("Book add in Library successfully.")

    def return_book(self, book):
        self.lend_dict.pop(book)
        time.sleep(3)
        print("Book return is successfully.")


if __name__ == '__main__':
    vishal = Library(["Rich dad Poor dad", "Python Basics", "C++ Basics", "Juman Ji", "Java"], "Vishal")
    print(f"Welcome to the {vishal.name} Library")
    while True:
        print("Press \n1.Display Book \n2.Lend Book \n3.Add Book \n4.Return Book \nQ.Quit")
        user_chose = input("Enter here:")
        if user_chose == "1":
            vishal.display_book()
        elif user_chose == "2":
            book_name = input("Enter Book name which you book lend:")
            user_name = input("Enter your name:")
            vishal.lend_book(book_name, user_name)
        elif user_chose == "3":
            book_name = input("Enter Book name which you book add in library:")
            vishal.add_book(book_name)
        elif user_chose == "4":
            book_name = input("Enter Book name:")
            vishal.return_book(book_name)
        elif user_chose == "Q" or user_chose == "q":
            break

        else:
            print("choose valid option")
        time.sleep(5)
