from app import books

USER_CHOICE = '''Enter one of the following
- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the page
- 't' to get total count of books
- 'q' to exit
Enter your choice: '''

def print_best_books():
    best_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10] # multiple soring.
    for book in best_books:
        print(book)

def print_cheapest_books():
    best_books = sorted(books, key=lambda x: x.price)[:5]
    for book in best_books:
        print(book)

def print_books_count():
    print(len(books))

books_generator = (x for x in books)
def print_next_book():
    print(next(books_generator))

user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': print_next_book,
    't': print_books_count
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n', 't'):
            user_choices[user_input]()
        elif user_input == 'q':
            exit(0)
        else:
            print('invalid entry {}'.format(user_input))
        user_input = input(USER_CHOICE)

menu()