import random
import hangman_art
import hangman_wordlist

print(hangman_art.logo)
name = input("What is Your Name? ")
print(f"Good Luck {name}!")

lives = 6
random_number = random.choice(list(hangman_wordlist.word_list.items()))
chosen_word = random_number[0]
hint = random_number[1]

display =[]
for letter in chosen_word:
    display += "_"
print(display)
end_of_game = False
while not end_of_game:
    print(f"Hint:{hint}")
    guess = input("Guess the character: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(f"You have {lives}  guesses left!")
        if lives == 0:
            end_of_game = True
            print("Wrong guess, You are hanged!")
            print(f"The word was: {chosen_word}")

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You Win")
        print(f"The word is: {chosen_word}")
    print(hangman_art.stages[lives])
