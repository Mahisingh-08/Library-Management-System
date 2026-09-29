from data import books, students, issued_books

# Generate library report
def library_report():
    total_books = len(books)
    available_books = 0
    issued = len(issued_books)
    total_students = len(students)

    for book in books:
        if book["available"] == True:
            available_books = available_books + 1

    print("\n========== LIBRARY REPORT ==========")
    print("Total Books:", total_books)
    print("Available Books:", available_books)
    print("Issued Books:", issued)
    print("Total Students:", total_students)
    print("====================================")