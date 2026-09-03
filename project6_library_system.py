#Project 6: Mini Library Management System

print("Welcome to the Mini Library Management System!")

library = {
    "python101": "Available",
    "datascience": "Available",
    "algorithms": "Available"
}

borrowed_books = set()

while True:
    print("\n--- Mini Library Menu Management System ---")
    print("1 - Add Book")
    print("2 - Borrow Book")
    print("3 - Return Book")
    print("4 - View All Books")
    print("5 - Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        print("Add Book:")

        book_name = input("Enter the name of the book to add: ")
        if book_name in library:
            print(f"{book_name} already exists in the library.")
        else:
            library[book_name] = "Available"
            print(f"{book_name} has been added to the library.")

    elif choice == "2":
        print("Borrow Book:")

        book_name = input("Enter the name of the book to borrow: ")
        if book_name in library and library[book_name] == "Available":
            library[book_name] = "Borrowed"
            borrowed_books.add(book_name)
            print(f"You have borrowed {book_name}.")
        else:
            print(f"{book_name} is not available for borrowing.")

    elif choice == "3":
        print("Return Book:")

        book_name = input("Enter the name of the book to return: ")
        if book_name in borrowed_books:
            library[book_name] = "Available"
            borrowed_books.remove(book_name)
            print(f"You have returned {book_name}.")
        else:
            print(f"{book_name} was not borrowed from this library.")

    elif choice == "4":
        print("\n--- Library Books ---")
        borrowed_books = []
        available_books = []

        for book, status in library.items():
            print(f"{book.title()}: {status}")

            if status == "Borrowed":
                borrowed_books.append(book)
            else:
                available_books.append(book)

        print("\n--- Statistics Books ---")

        print(f"Total books in library: {len(library)}")
        print(f"Available books: {(available_books)} - length: {len(available_books)}")
        print(f"Borrowed books: {(borrowed_books)} - length: {len(borrowed_books)}")

    elif choice == "5":
        print("Exiting the Mini Library Management System. Goodbye!")
        break

    else:
        print("Invalid option. Please choose a number between 1 and 5.")
