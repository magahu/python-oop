from cats_book import Cat
from cats_book import Book

def main():

    cats_book = Book()


    while True:

        op = input('''
        Select one option:

        [C] Create cat
        [S] Show cats
        [U] Update cat
        [D] Delete cat
        [E] EXIT

        Enter your option: ''').upper()

        if op == 'C':
            cats_book.add_cat()

        elif op == 'S':
            cats_book.show_cats()

        elif op == 'U':
            id_to_update = input('Enter cat ID to update: ')
            cats_book.update_cat(id_to_update)

        elif op == 'D':
            cats_book.delete_cat()

        elif op == 'E':
            break

        else:
            print('PLEASE, ENTER A VALID OPTION')


if __name__ == '__main__':
    main()
