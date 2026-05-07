import random
someWords = ["apple","banana","mango","strawberry","orange","grape","pineapple","apricot","lemon","coconut","watermelon","cherry","papaya","berry","peach","lychee","muskmelon"]
word = random.choice(someWords)
def draw_hangman(chances):
    if chances == 5:
        print("--------")
        print("   |  |")
        print("   o  |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif chances == 4:
        print("--------")
        print("   |  |")
        print("   o  |")
        print("   |  |")
        print("      |")
        print("      |")
        print("=========")
    elif chances == 3:
        print("--------")
        print("   |  |")
        print("   o  |")
        print("  /|  |")
        print("      |")
        print("      |")
        print("=========")
    elif chances == 2:
        print("--------")
        print("   |  |")
        print("   o  |")
        print("  /|\ |")
        print("      |")
        print("      |")
        print("=========")
    elif chances == 1:
        print("--------")
        print("   |  |")
        print("   o  |")
        print("  /|\ |")
        print("  /   |")
        print("      |")
        print("=========")
    elif chances == 0:
        print("--------")
        print("   |  |")
        print("   o  |")
        print("  /|\ |")
        print("  / \ |")
        print("      |")
        print("=========")
if __name__ == '__main__':
    print('Guess the word! HINT: word is a fruit.')
    letterGuessed = ''
    chances = 6   
    flag = 0
    print("--------")
    print("   |  |")
    print("      |")
    print("      |")
    print("      |")
    print("      |")
    print("=========")
    try:
        while chances > 0 and flag == 0:
            print("\nChances left:", chances)
            guess = input('Enter a letter to guess: ').lower()
            if not guess.isalpha():
                print('Enter only a letter!')
                continue
            elif len(guess) > 1:
                print('Enter only a single letter!')
                continue
            elif guess in letterGuessed:
                print('You already guessed that letter!')
                continue
            if guess in word:
                letterGuessed += guess * word.count(guess)
            else:
                chances -= 1
                print("Wrong guess!")
                draw_hangman(chances)
            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                else:
                    print('_', end=' ')
            print()
            if Counter(letterGuessed) == Counter(word):
                print("\nCongratulations! You guessed the word:", word)
                flag = 1
                break

        if chances <= 0 and Counter(letterGuessed) != Counter(word):
            print('\nYou lost! The word was:', word)
    except KeyboardInterrupt:
        print('\nGame interrupted. Bye!')
