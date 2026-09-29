from data import books

# Add a new book
def add_book():
    book_id = int(input("Enter book ID: "))

    for book in books:
        if book["id"] == book_id:
            print("Book ID already exists.")
            return

    title = input("Enter book title: ")
    author = input("Enter author name: ")

    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(new_book)

    print("Book added successfully!")

# Display all books
def view_books():
    print("\n----- BOOK LIST -----")

    for book in books:
        print("ID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])

        if book["available"]:
            print("Status: Available")
        else:
            print("Status: Issued")

        print("--------------------")

# Search for a book by title
def search_book():
    name = input("Enter book title to search: ")

    found = False

    for book in books:
        if book["title"].lower() == name.lower():
            print("\nBook Found!")
            print("ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])

            if book["available"]:
                print("Status: Available")
            else:
                print("Status: Issued")

            found = True

    if found == False:
        print("Book not found.")


        