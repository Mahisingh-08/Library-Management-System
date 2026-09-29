# Main program and menu
from books import add_book, view_books, search_book
from students import add_student, view_students
from issue_return import issue_book, return_book
from reports import library_report


while True:
    print("\n================================")
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Add Student")
    print("5. View Students")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Library Report")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        add_student()

    elif choice == "5":
        view_students()

    elif choice == "6":
        issue_book()

    elif choice == "7":
        return_book()

    elif choice == "8":
        library_report()

    elif choice == "9":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 9.")