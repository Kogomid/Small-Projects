import random
from words_hangman import words

word = words[random.randrange(2643)].lower()

def hangman_template(word):
    return ["_" for _ in range(len(word))]


def hangman(word):
    guessed = []
    guessed_wrong = []
    guess_tries = 0
    GUESS_LIMIT = 12

    template = hangman_template(word)
    print(" ".join(template))

    while "_" in template and guess_tries != GUESS_LIMIT:
        guesses_left = GUESS_LIMIT - guess_tries - 1
        guess_letter = input("Wpisz literę: ").lower().rstrip()

        if guess_letter.isalpha and len(guess_letter) == 1:
            if guess_letter in guessed or guess_letter in guessed_wrong:
                print("Już użyłeś tej litery")
                print(" ")
                continue
        
            if guess_letter in word:
                print("Zgadłeś.")                  
                for i in range(len(word)):
                    if word[i] == guess_letter:
                        template[i] = guess_letter                      
                guessed.append(guess_letter)          
            else:
                print("Zła odpowiedź")
                guessed_wrong.append(guess_letter)
                guess_tries += 1
                
            print(" ".join(template))
            print(f"Zostało {guesses_left} prób")
            print(" ")
            
        else:
            print("Wpisz pojedynczą literę.")
        
    if "_" not in template:
        print("Wygrałeś!")
    else:
        print("Przegrałeś :(")
        

def main():
    word = random.choice(words)
    hangman(word)


main()
