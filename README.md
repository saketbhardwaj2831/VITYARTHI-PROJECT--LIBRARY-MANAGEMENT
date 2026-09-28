# VIT Bhopal Library Management System

## 1. Project Title

VIT Bhopal Library Management System

## 2. Overview of the Project

This is a simple Python-based Library Management System for managing books and library members.

The program allows a librarian to:

- Add and remove books

- Search for books by title or author

- View available books

- Register and view members

- Issue and return books

- Calculate fines for late returns

- Check overdue books

- View total fines and library summary

- View an activity log

The system begins with a password for the librarian and provides a menu of options for the librarians to choose from. The current program uses sample VIT Bhopal library data and stores the information while the program is running.

## 3. Features

### Librarian Login

- Password protected access

- Up to 5 login attempts

- Current password in the program: `vit123`

### Book Management

- Add a new book

- Remove a book

- Cannot add duplicate book IDs

- Cannot remove a book that is currently issued

- View all books and available copies

- Search books by title or author

### Member Management

- Register new library members

- Validate registration number format

- View registered members

- Display the number of books currently held by each member

### Issue and Return

- Issue books to registered members

- Check book availability

- Limit each member to a maximum of 5 books

- A member cannot issue the same book twice

- Return issued books

- Automatically update available copies

### Fine Management

- Loan period: 14 days

- Rs 2 fine per late day

- Calculated fine when a book is returned

- View accumulated fines

- Generate an overdue report

### Summary and Log

- Display total book titles

- Display copies currently on the shelf

- Display number of issued books

- Display number of registered members

- Keep a simple activity log of book and member operations

## 4. Technologies / Tools Used

- Python 3

- Python dictionaries for storing books, members, issued books and fines

- Python lists for maintaining the activity log

- Functions for different library operations

- `input()` and `print()` for user interaction

- VS Code or any Python-compatible IDE

- Command Prompt / Terminal for running the program

No external Python libraries are required.

## 5. Steps to Install & Run the Project

### Step 1: Install Python

Install Python 3 on your computer.

Check whether Python is installed by opening Command Prompt or Terminal and typing:

```bash

python --version

```

### Step 2: Open the Project

Place the Python file in a folder, for example:

```text

Library Management System/

└── main.py

```

Open this folder in VS Code.

### Step 3: Run the Program

Open the VS Code terminal and run:

```bash

python main.py

```

If your computer uses `python3`, use:

```bash

python3 main.py

```

### Step 4: Login

When the program asks for the librarian password, enter:

```text

vit123

```

After successful login, the main menu will appear.

## 6. Instructions for Testing

Use the following steps to test the main features.

### Test 1: View Books

1. Start the program.

2. Enter the password `vit123`.

3. Select option `4`.

4. Check that the available books are displayed.

The initial books include:

- CSE1021 - Python Basics

- MAT1003 - Engineering mathematics

- ENG1005 - Harry Potter

### Test 2: Add a Member

1. Select option `5`.

2. Enter a valid registration number such as:

`24BCE10001`

3. Enter the member's name.

4. The program should display:

`Member registered.`

### Test 3: Search for a Book

1. Select option `3`.

2. Enter a title or author name, such as:

`Python`

3. The matching book should be displayed.

### Test 4: Issue a Book

1. First register a member.

2. Select option `7`.

3. Enter the registered member's registration number.

4. Enter a valid book ID such as `CSE1021`.

5. Enter today's day number, for example `10`.

6. The program should issue the book and display its due day.

The normal loan period is 14 days.

### Test 5: Return a Book

1. Select option `8`.

2. Enter the member registration number.

3. Enter the book ID.

4. Enter the return day number.

5. The program should calculate and display the fine, if any.

For example, if a book is issued on day `10` and returned on day `30`:

```text

Late days = 30 - 10 - 14 = 6

Fine = 6 × Rs 2 = Rs 12

```

### Test 6: Check Overdue Books

1. Select option `9`.

2. Enter today's day number.

3. The program will display books that are overdue and the fine accumulated so far.

### Test 7: View Fines

1. Select option `10`.

2. The program displays fines recorded for members and the total fine.

### Test 8: View Summary

1. Select option `11`.

2. Check the total number of titles, copies on the shelf, issued books and members.

### Test 9: View Activity Log

1. Perform some operations such as adding a member or issuing a book.

2. Select option `12`.

3. The program displays the recorded activities.

## 7. Main Menu

After login, the program provides these options:

```text

1 Add book

2 Remove book

3 Search book

4 View books

5 Add member

6 View members

7 Issue book

8 Return book

9 Overdue

10 Fines

11 Summary

12 Log

0 Exit

```

## 8. Important Project Details

- Maximum books a member can borrow: 5

- Loan period: 14 days

- Fine per late day: Rs 2

- Maximum incorrect password attempts: 5

- Librarian password: `vit123`

## 9. Screenshots

Screenshots of the program's execution can be added here to show:

- Librarian login

- Main menu

- Book list

- Member registration

- Book issue

- Book return and fine

- Overdue report

- Library summary

Example:

```text

[Add your program screenshots here]

```

## 10. Project File Structure

```text

Library Management System/

│

├── main.py

└── README.md

```

main.py contains the complete Python program.

README.md contains the project description, features, setup instructions and testing instructions.