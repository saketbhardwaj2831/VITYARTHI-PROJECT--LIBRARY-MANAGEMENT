LOAN_DAYS = 14
FINE_PER_DAY = 2
MAX_BOOKS = 5
PASSWORD = "vit123"

books = {
    "CSE1021": {"title": "Python Basics", "author": "Guido Rossum", "copies": 20},
    "MAT1003": {"title": "Engineering mathematics ", "author": "BS greval", "copies": 25},
    "ENG1005": {"title": "Harry Potter", "author": "JK Rowling", "copies": 30},
}
members = {}    # reg_no -> name
issued = {}     # (reg_no, book_id) -> issue day
fines = {}      # reg_no -> total fine
log = []


def get_int(number):
    value = input(number).strip()
    while not value.isdigit():
        value = input("Enter a number: ").strip()
    return int(value)


def valid_registration_no(reg):
    # format like 24BCE10001
    return len(reg) == 10 and reg[:2].isdigit() and reg[2:5].isalpha() and reg[5:].isdigit()


def login():
    for i in range(5):
        if input("Enter librarian password: ") == PASSWORD:
            return True
        print("Wrong password.")
    return False


def add_book():
    book_id = input("Book ID: ").strip().upper()
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    copies = input("Copies: ").strip()
    if book_id == "" or title == "" or book_id in books:
        print("Invalid or duplicate book ID.")
    elif not copies.isdigit() or int(copies) < 1:
        print("Copies must be a positive number.")
    else:
        books[book_id] = {"title": title, "author": author, "copies": int(copies)}
        log.append("Added book " + book_id)
        print("Book added.")


def remove_book():
    book_id = input("Book ID to remove: ").strip().upper()
    if book_id not in books:
        print("Book not available.")
        return
    for (reg, bid) in issued:
        if bid == book_id:
            print("Book is currently issued. Cannot remove.")
            return
    del books[book_id]
    log.append("Removed book " + book_id)
    print("Book removed.")


def show_books(id_list):
    if len(id_list) == 0:
        print("No books available.")
    for bid in id_list:
        b = books[bid]
        print(bid, "|", b["title"], "|", b["author"], "| Copies:", b["copies"])


def search_books():
    keyword = input("Search title/author: ").strip().lower()
    found = []
    for bid in books:
        if keyword in books[bid]["title"].lower() or keyword in books[bid]["author"].lower():
            found.append(bid)
    show_books(found)


def add_member():
    reg = input("Reg no (e.g. 24BCE10001): ").strip().upper()
    name = input("Name: ").strip()
    if not valid_registration_no(reg):
        print("Invalid registration number.")
    elif reg in members:
        print("Member already registered.")
    elif name == "":
        print("Name cannot be empty.")
    else:
        members[reg] = name
        log.append("Registered member " + reg)
        print("Member registered.")


def count_borrowed(reg):
    count = 0
    for (r, b) in issued:
        if r == reg:
            count += 1
    return count


def show_members():
    if len(members) == 0:
        print("No members yet.")
    for reg, name in members.items():
        print(reg, "-", name, "| Books held:", count_borrowed(reg))


def calculate_fine(issue_day, return_day):
    late_days = return_day - issue_day - LOAN_DAYS
    if late_days > 0:
        return late_days * FINE_PER_DAY
    return 0


def issue_book():
    reg = input("Reg no: ").strip().upper()
    bid = input("Book ID: ").strip().upper()
    day = get_int("Today's day number: ")
    if reg not in members:
        print("Member not registered.")
    elif bid not in books:
        print("Book not found.")
    elif books[bid]["copies"] == 0:
        print("No copies available.")
    elif (reg, bid) in issued:
        print("Student already has this book.")
    elif count_borrowed(reg) >= MAX_BOOKS:
        print("Borrow limit reached.")
    else:
        issued[(reg, bid)] = day
        books[bid]["copies"] -= 1
        log.append(reg + " issued " + bid + " on day " + str(day))
        print("Book issued. Due on day", day + LOAN_DAYS)


def return_book():
    reg = input("Reg no: ").strip().upper()
    bid = input("Book ID: ").strip().upper()
    day = get_int("Today's day number: ")
    if (reg, bid) not in issued:
        print("No such issue record.")
    elif day < issued[(reg, bid)]:
        print("Return day cannot be before issue day.")
    else:
        fine = calculate_fine(issued[(reg, bid)], day)
        del issued[(reg, bid)]
        books[bid]["copies"] += 1
        fines[reg] = fines.get(reg, 0) + fine
        log.append(reg + " returned " + bid + " fine Rs" + str(fine))
        print("Book returned. Fine: Rs", fine)


def summary():
    total = 0
    for bid in books:
        total += books[bid]["copies"]
    print("Titles:", len(books), "| Copies on shelf:", total,
          "| Issued:", len(issued), "| Members:", len(members))


def overdue_report():
    today = get_int("Today's day number: ")
    found = False
    for (reg, bid), day in issued.items():
        late = today - day - LOAN_DAYS
        if late > 0:
            print(reg, "overdue", bid, "by", late, "days. Fine so far: Rs", late * FINE_PER_DAY)
            found = True
    if not found:
        print("No overdue books.")


def fine_report():
    total = 0
    for reg, amount in fines.items():
        print(reg, "- Rs", amount)
        total += amount
    print("Total fines: Rs", total)


def show_log():
    if len(log) == 0:
        print("Log is empty.")
    i = 1
    for entry in log:
        print(i, entry)
        i+=1



def menu():
    print("\n===== VIT Bhopal Library =====")
    print("1 Add book    2 Remove book   3 Search book   4 View books")
    print("5 Add member  6 View members  7 Issue book    8 Return book")
    print("9 Overdue    10 Fines        11 Summary      12 Log     0 Exit")


def main():
    if not login():
        print("Too many wrong attempts.")
        return
    running = True
    while running:
        menu()
        choice = get_int("Choice: ")
        if choice == 1:
            add_book()
        elif choice == 2:
            remove_book()
        elif choice == 3:
            search_books()
        elif choice == 4:
            show_books(list(books))
        elif choice == 5:
            add_member()
        elif choice == 6:
            show_members()
        elif choice == 7:
            issue_book()
        elif choice == 8:
            return_book()
        elif choice == 9:
            overdue_report()
        elif choice == 10:
            fine_report()
        elif choice == 11:
            summary()
        elif choice == 12:
            show_log()
        elif choice == 0:
            print("Thank you!")
            running = False
        else:
            print("Invalid choice.")


main()