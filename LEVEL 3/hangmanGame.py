import random

easy_foods = [
    "Apple", "Banana", "Orange", "Grape", "Strawberry", "Blueberry", "Mango",
    "Pineapple", "Watermelon", "Lemon", "Carrot", "Potato", "Tomato", "Onion",
    "Broccoli", "Spinach", "Lettuce", "Cucumber", "Coconut", "Corn", "Pumpkin",
    "Pea", "Bean", "Mushroom", "Garlic", "Dates", "Cabbage", "Avocado", "Cherry"
]

medium_foods = [
    "Plum", "Kiwi", "Raspberry", "Grapefruit", "Apricot", "Eggplant",
    "Guava", "Cauliflower", "Jackfruit", "Radish", "Okra", "Ginger",
    "Cranberry", "Beetroot", "Capsicum", "Drumstick", "Gourd"
]

def play_round(playername):
    level, word = "", ""

    while True:
        print(f"\n{playername}, please choose your game level.")
        level_input = input("(Easy or Medium (E/M)): ").strip().lower()

        if level_input in ['easy', 'e', '1']:
            level = "e"
            word = random.choice(easy_foods).lower()
            break
        elif level_input in ['medium', 'm', '2']:
            level = "m"
            word = random.choice(medium_foods).lower()
            break
        else:
            print("Type E for Easy or M for Medium level. Try Again.")

    l = len(word)

    chances = l + 3 if level == "e" else l + 2 
    guessed_letters = set()
    display_word = ['_'] * l

    print(f"\n--- New Round Started ---")
    print(f"Guess the {l}-letter word within {chances} total guesses.")
    print(" ".join(display_word))

    i = 0
    while chances > 0 and "".join(display_word) != word:
        i += 1

        while True:
            letter = input(f'\nChance No. {i} (Remaining: {chances}): ').strip().lower()

            if not letter.isalpha() or len(letter) != 1:
                print('Enter only a single letter!')
            elif letter in guessed_letters:
                print(f"You already guessed '{letter}'. Try a new letter.")
            else:
                guessed_letters.add(letter)
                break

        chances -= 1

        if letter in word:
            print(f"✅ Correct! '{letter}' is in the word.")

            for index, char in enumerate(word):
                if char == letter:
                    display_word[index] = letter
            print(" ".join(display_word))

            if "".join(display_word) == word:
                print("\n🎉 CONGRATULATIONS! You guessed the word!")
                print(f"The word was: {word.upper()}")
                return True 
        else:
            print(f"❌ Incorrect! '{letter}' is not in the word. Chances left: {chances}")
            print(" ".join(display_word))

    if chances == 0 and "".join(display_word) != word:
        print("\n😢 GAME OVER! You ran out of chances.")
        print(f"The word was: {word.upper()}")
        return False 

if __name__ == "__main__":
    player_name = input("Welcome! Enter your name: ").strip()

    while True:

        play_round(player_name) 

        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print(f"\nThanks for playing, {player_name}! Goodbye.")
            break
