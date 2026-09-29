# Library Management System - Test Cases

## 1. View Books

**Input:** Choose option 2

**Expected Output:** The system displays all available books with their ID, title, author, and status.

**Result:** Passed

---

## 2. Add Book

**Input:** Choose option 1 and enter a new book ID, title, and author.

**Expected Output:** The new book is added successfully.

**Result:** Passed

---

## 3. Search Book

**Input:** Choose option 3 and enter an existing book title.

**Expected Output:** The system displays the book details.

**Result:** Passed

---

## 4. Search Invalid Book

**Input:** Choose option 3 and enter a book title that does not exist.

**Expected Output:** The system displays "Book not found."

**Result:** Passed

---

## 5. Add Student

**Input:** Choose option 4 and enter student ID, name, and course.

**Expected Output:** The student is added successfully.

**Result:** Passed

---

## 6. View Students

**Input:** Choose option 5.

**Expected Output:** The system displays the list of students.

**Result:** Passed

---

## 7. Issue Book

**Input:** Choose option 6 and enter a valid book ID and student ID.

**Expected Output:** The book is issued successfully and its status changes to Issued.

**Result:** Passed

---

## 8. Issue Already Issued Book

**Input:** Try to issue a book that is already issued.

**Expected Output:** The system displays "Book is already issued."

**Result:** Passed

---

## 9. Return Book

**Input:** Choose option 7 and enter the ID of an issued book.

**Expected Output:** The book is returned successfully and its status changes to Available.

**Result:** Passed

---

## 10. Library Report

**Input:** Choose option 8.

**Expected Output:** The system displays total books, available books, issued books, and total students.

**Result:** Passed

---

## 11. Invalid Menu Choice

**Input:** Enter a number outside 1 to 9.

**Expected Output:** The system displays "Invalid choice."

**Result:** Passed

---

## 12. Exit

**Input:** Choose option 9.

**Expected Output:** The system displays a thank-you message and exits.

**Result:** Passed
