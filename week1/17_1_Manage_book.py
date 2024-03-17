def book_management():
    IDs = []
    titles= []
    authors= []
    Available_status= []
    running = True
    while running:
        menu()
        choice = int(input('Enter your choice: '))
    if choice == 1:
        add_book(IDs, titles, authors, Available_status)
    elif choice == 2:
        search_book(IDs, titles, authors, Available_status)
    elif choice == 3:
        search_book_by_title(titles, authors, Available_status)
    elif choice == 4:
        sort_books_by_title(IDs, titles, authors, Available_status)  # New option for sorting by title
    elif choice == 5:
        edit_book(IDs, titles, authors, Available_status)
    elif choice == 6:
        delete_book(IDs, titles, authors, Available_status)
    elif choice == 7:
        display_book(IDs, titles, authors, Available_status)
    elif choice == 8:
        borrow_book(IDs, titles, authors, Available_status)
    elif choice == 9:
        return_book(IDs, titles, authors, Available_status)
    elif choice == 10:
        print('Thank you! ')
        running = False
    else:
        print('Invalid choice. Try again')
def menu():
    print('1. Add book')
    print('2. Search book by ID')
    print('3. Search book by title')
    print('4. Sort books by title')  
    print('5. Edit book')
    print('6. Delete books')
    print('7. Display book')
    print('8. Borrow program')
    print('9. Return books')
    print('10. Quit')


def add_book(IDs,titles, authors, Available_status ):
    id = int(input('Enter ID: '))
    title = input('Enter book name: ')
    author = input('Enter author: ')
    available = input('Enter status: ')
    IDs.append(id)
    titles.append(title)
    authors.append(author)
    Available_status.append(available)
    print(f'Book number {id} has been added')

def search_book(IDs, titles, authors, Available_status):
    id = int(input('Enter ID: '))
    for i in range(len(IDs)):
        if IDs[i] == id:
            print(f'Found: | ID:  {IDs[i]} | Title: {titles[i]} | Author: {authors[i]} | Status" {Available_status[i]} |')
        else:
            print('Not found')

def search_book_by_title(titles, authors, Available_status):
    title_to_search = input('Enter the title of the book: ')
    found_books = []

    for i in range(len(titles)):
        if title_to_search.lower() in titles[i].lower():
            found_books.append(i)

    if found_books:
        print('\nFound Books:')
        for i in found_books:
            print('ID:', IDs[i])
            print('Title:', titles[i])
            print('Author:', authors[i])
            print('Available:', 'Yes' if Available_status[i] else 'No')
            print('---')
    else:
        print('No books found with the given title.')   

def edit_book(IDs, titles, authors, Available_status):
    id = int(input('Enter ID: '))
    new_title = input('Enter new title: ')
    new_author = input('Enter new author: ')
    for i in range(len(IDs)):
        if IDs[i] == id:
            titles[i] = new_title
            authors[i] = new_author
            print(f'The book number {id} has been edited')
            return
        else:
            print(f'The book number {id} not found')

def delete_book(IDs, titles, authors, Available_status):
    id = int(input('Enter ID: '))
    for i in range(len(IDs)):
        if IDs[i] == id:
            IDs.pop(i)
            titles.pop(i)
            authors.pop(i)
            Available_status.pop(i)
            print(f'The book number {id} has been delete')
            return
        else:
            print(f'The book number {id} not found')

def display_book(IDs, titles, authors, Available_status):
    for i in range(len(IDs)):
        print(f'| ID: {IDs[i]} | Title: {titles[i]} | Author: {authors[i]} | Available: {Available_status[i]} ')

def borrow_book(IDs, titles, authors, Available_status):
    id = int(input('Enter ID: '))
    for i in range(len(IDs)):
        if IDs[i] == id:
            Available_status[i] = 'no'
            return
        else:
            print(f'The book number {id} not found')
def return_book(IDs, titles, authors, Available_status):
    id = int(input('Enter ID: '))
    for i in range(len(IDs)):
        if IDs[i] == id:
            Available_status[i] = 'yes'
            return
        else:
            print(f'The book number {id} not found')

def sort_books_by_title(IDs, titles, authors, Available_status):
    sorted_indices = sorted(range(len(titles)), key=lambda i: titles[i].lower())
    
    print('\nBooks Sorted by Title:')
    for i in sorted_indices:
        print('ID:', IDs[i])
        print('Title:', titles[i])
        print('Author:', authors[i])
        print('Available:', 'Yes' if Available_status[i] else 'No')
        print('---')
    
book_management()