# TextAnalyzer by P8(Eduardo Schneider)

# Feature 1: Get input
user_sen = input("Enter a sentence to analyze: ")
print(user_sen)

# Feature 2: Basic stats
print()
characters = len(user_sen)
print(f"Total of characters: {characters}")

word_list = user_sen.split()
words_count = len(word_list)
print(f"Total of words: {words_count}")

# Feature 3: Case transformations
print()
print(f"Uppercase: {user_sen.upper()}")
print(f"Lowercase: {user_sen.lower()}")
print(f"Capitalized: {user_sen.capitalize()}")

# Feature 4: Vowel counter
print()
vowels = ("a", "e", "i", "o", "u")

vowel_count = 0
vowel_list = []
for char in user_sen:
    if char.lower() in vowels:
        vowel_list.append(char)
        vowel_count += 1

print(f"Number of Vowels: {vowel_count}")
print(f"Vowels Found: {vowel_list}")

# Feature 5: Space counter
print()
space_counter = 0
for char in user_sen:
    if char == " ":
        space_counter += 1

print(f"Number of Spaces: {space_counter}")

# Feature 6 & 7 (NO WAY!!! :0): Letter counter with quit option
print()
while True:
    letter_to_find = input("Which letter should I count? (Type 'quit' to QUIT): ")

    if letter_to_find.lower() == "quit":
        print("Thanks for testing P8's text analyzer!")
        break

    letter_counter = 0
    for char in user_sen:
        if char == letter_to_find:
            letter_counter += 1

    print(f"The letter '{letter_to_find}' appears {letter_counter} times.")
    print(f"Sentence: {user_sen}\n")