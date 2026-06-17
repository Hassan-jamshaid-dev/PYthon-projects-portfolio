# HANGMAN PROGRAM


import  random
from operator import index

words = ("apple", "burger","man","portugal","apricot","messi")
art_a = {0:("   ",
            "    ",
            "    "),
         1:(" o ",
            "   ",
            "   "),
        2: (" o ",
            " | "),
        3: (" o ",
            "|\\",
            "   "),
         4: (" o ",
             "/|\\",
             "   "),
        5: (" o ",
           "/|\\",
           "/   ") ,
       6 : (" o ",
            "/|\\ ",
            "/ \\")}

def hint_man(hint):
    print(" ".join(hint))


def display_man(wrong_guesses):
    for line in art_a[wrong_guesses]:
        print(line)
    print("--------------------------")
    print()


def answer_man(answer):
    print(" ".join(answer))


def main():
   answer = random.choice(words)
   hint = ["_"] * len(answer)
   wrong_guesses = 0
   guessed_letters = set()
   is_running = True


   while is_running:
       print("--------HANGMAN GAME--------")
       display_man(wrong_guesses)
       hint_man(hint)
       guess = input("Enter a letter to guess the word: ").lower()

       if len(guess) != 1:
           print("Your guess cannot be more than 1 letter!")
           continue
       if  not   guess.isalpha():
           print("You can only choose letters")
           continue
       if guess in guessed_letters:
           print("You cannot guess a letter more than once")
           continue


       guessed_letters.add(guess)



       if guess in answer:
           for index in range(len(answer)):
               if answer[index] == guess:
                   hint[index] = guess

       else:
           wrong_guesses+=1

       if "_" not in hint:
           display_man(wrong_guesses)
           answer_man(answer)
           print("YOU WIN!")
           is_running = False

       elif wrong_guesses >= len(art_a) - 1:
           display_man(wrong_guesses)
           answer_man(answer)
           print("YOU LOSE!!")
           is_running = False









if __name__ == "__main__":
    main()
