def change_letter_list(letter_list, word):
    starting = len(letter_list)
    repeat_letters = []

    for letter in word:
        if not letter in repeat_letters:
            repeat_letters.append(letter)
            if letter in letter_list:
                letter_list.remove(letter)
            else:
                letter_list.append(letter)

    ending = len(letter_list)
    difference = ending - starting
    return difference

print("---------------------")
print("INSTRUCTIONS:")
print()
print("Type a word.")
print("If a letter in your word is already in the list, it will be removed.")
print("If that letter is not already in the list, it will be added.")
print("Try to get the list as big as possible using only real words.")
print("---------------------")
print()

letters = []
max_length = 0
playing = True

while playing:

    print("The following letters are in the list: ")
    print(letters)

    next_word = input("Enter a word: (x to quit) ")
    print()

    if next_word == "x":
        break

    else:
        length_change = change_letter_list(letters, next_word)
        if length_change > 0:
            print("Congrats! You added letters to the list!")
            max_length = len(letters)
        elif length_change < 0:
            print("Oops, you made the list shorter.")

print()
print("Your final list length was " + str(len(letters)))
print("Your longest list length was " + str(max_length))
