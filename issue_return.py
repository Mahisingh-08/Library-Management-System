from data import books, students, issued_books

# Issue a book to student
def issue_book():
    book_id = int(input("Enter book ID: "))
    student_id = int(input("Enter student ID: "))

    book_found = False
    student_found = False

    for book in books:
        if book["id"] == book_id:
            book_found = True

            if book["available"] == False:
                print("Book is already issued.")
                return

            for student in students:
                if student["id"] == student_id:
                    student_found = True

                    book["available"] = False

                    record = {
                        "book_id": book_id,
                        "student_id": student_id
                    }

                    issued_books.append(record)

                    print("Book issued successfully!")
                    return

    if book_found == False:
        print("Book not found.")

    if student_found == False:
        print("Student not found.")

# Return an issued book
def return_book():
    book_id = int(input("Enter book ID to return: "))

    found = False

    for record in issued_books:
        if record["book_id"] == book_id:

            for book in books:
                if book["id"] == book_id:
                    book["available"] = True

            issued_books.remove(record)

            print("Book returned successfully!")
            found = True
            return

    if found == False:
        print("This book is not currently issued.")