
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