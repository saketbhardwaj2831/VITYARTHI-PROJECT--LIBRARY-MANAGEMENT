# Project Statement

## 1. Problem Statement

Manually managing a library can cause many problems such as maintaining a record of books, members, issued books with their issue and return dates, overdue books, fines, etc.

The proposed project aims at providing a simple python based Library Management System for VIT Bhopal which will aid the librarian to maintain books and members, issue and return books, calculate fines and view various reports in a form of a menu driven program.

## 2. Scope of the Project

The project will have the following features which will help in managing a library:

- Login as a librarian with a password.

- Add new books, and remove books.

- Search books by title or author.

- View all the books with their copies.

- Register and view members.

- Issue and return books.

- Set loan period as 14 days.

- Set fine for late return as 2 rupees per day.

- Set limit of 5 books for a member.

- View reports of overdue books and fine.

- View summary of the library.

- Maintain a simple log of activities.

The system will be a simple menu driven console python application and will maintain its data in memory for the time that it is running.

## 3. Target Users

There are three types of target users for the project:

- Librarians : This includes everyone who has a role in managing books and members of the library. This involves adding and removing books, adding and removing members, issuing and returning books, maintaining fines and viewing reports.

- Library staff: This involves people who work in the library, but do not manage books or members. They will be managing the day to day operations of the library.

- Students / library members: This involves all the students who will be using the library. They will be registering as members, and issuing and returning of books will be tracked for them.

## 4. High-Level Features

### 🔐 Librarian Login

- Login to the library portal with a password.

- 5 attempts are given to login.

### 📚 Book Management

- Adding a new book in the library with book id, title, author, number of copies.

- Removing a book from the library if it is not issued.

- Searching a book with title or author.

- Viewing all the books and their available copies.

### 👥 Member Management

- Register a member with a registration number.

- Validate the registration number format.

- Viewing all the members and the number of books that they have.

### 📖 Issue and Return Books

- Issue a book only to a member.

- Check availability of a book.

- Do not allow a member to issue the same book again.

- Do not allow issuing more than 5 books to a member.

- Return a book and update the available copies of the book.

### 💰 Fine Management

- The loan period for issued books is 14 days.

- Fine for a late return is 2 rupees per day.

- View fine details for a member.

- View overdue books and the fine due on them.

### 📊 Reports and Activity Log

- View summary of the books, copies, issued books and members of the library.

- View a report of all the overdue books.

- View a summary of all the fines.

- Maintain a log of all the important activities like adding a book, registering a member, issuing a book, returning a book, etc.