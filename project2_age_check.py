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
