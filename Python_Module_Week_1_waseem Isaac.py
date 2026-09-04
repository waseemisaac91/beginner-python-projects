
#Werherer IT academy Bootcamp (VIT Program)
#Python_Module_Week_1
#Waseem Isaac
#29-8-2026
# Beginner Python Projects


#Project 1: Favorite Movie List

print("Welcome to the Favorite Movie List!")

movies = []
for i in range(3):
    movie = input(f"Enter the name of your favorite movie # {i+1}: ")
    movies.append(movie)

print("Your favorite movies are:", movies)
print("First movie:", movies[0] )
print("Last movie:", movies[-1])
print("Total number of movies:", len(movies))

#Project 2: Age Check

print("Welcome to the Age Check!")

while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

if age < 18:
    print("You are not an adult.")
else:
    print("You are an adult.")

birth_year = int(input("Enter your birth year: "))
while birth_year < 0 or birth_year > 2025:
    print("Invalid birth year. Please enter a valid birth year.")
    birth_year = int(input("Enter your birth year: "))

calculated_age = 2025 - birth_year
print("Your calculated age is:", calculated_age)

if calculated_age < 18:
    print("Based on birth year, you are not an adult.")
else:
    print("Based on birth year, you are an adult.")


#Project 3: Word Analysis Tool

print("Welcome to the Word Analysis Tool!")

user_input=input("Enter a sentence: ")

char_count = len(user_input.strip())
print("Number of characters in the sentence excluding spaces:", char_count)

word_count = len(user_input.split())
print("Number of words in the sentence:", word_count)

unique_words = set(user_input.split())
print("Number of unique words in the sentence:", len(unique_words))
print("Unique words:", unique_words)

#### longest_word = max(user_input.split(), key=len)

words = user_input.split()
longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("The longest word in the sentence is:", longest_word)

##Project 4: Mini Market Basket
print("Welcome to the Mini Market!")

products = {"apple": 3, "banana": 5, "bread": 2, "milk": 4}
basket = []
total_price = 0

while len(basket) < 3:
    product = input("Enter a product: ")
    if product in products:
        basket.append(product)
        total_price += products[product]
    else:
        print("warning - Product not found.")

print(f"Your basket: {', '.join(basket)}")
print(f"Total price: {total_price} TL")

#Project 5: Student Grading System

print("Welcome to the Student Grading System!")

students = {}

for i in range(3):
    print(f"Student {i+1}:")
    student_name = input("Enter student's name: ")
    grades = []

    for j in range(3):
        while True:
            try:
                grade = int(input(f"Enter grade {j+1} for {student_name}: "))
                if grade < 0 or grade > 100:
                    print("Grade must be between 0 and 100. Please enter a valid grade.")
                    continue
                grades.append(grade)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    students[student_name] = grades

averages = {}
for student, student_grades  in students.items():
        average_grade = sum(student_grades ) / len(student_grades )
        averages[student] = average_grade
        print(f"{student}'s average grade: {average_grade:.2f}")

highest_average = max(averages, key=averages.get)
print(f"\nStudent  with highest average: {highest_average} ({averages[highest_average]:.2f})")

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
