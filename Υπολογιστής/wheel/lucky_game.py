import random
import colorama
from colorama import Fore, Style
import time

cnt = 0
amount = 0
# ------------------------------------------------------------------------------------------------------------------
round_words = {"once in a blue moon": 200, "beat around the bush": 100, "executioner": 100, "medical": 100,
               "nightclub": 100, "stronghold": 100, "pregnancy": 200, "embezzle": 100,
               "razzmatazz": 100, "every cloud has a silver lining": 200, "photographer": 100,
               "unworthy": 200, "see eye to eye": 200, "kill two birds with one stone": 200, "wildlife": 100,
               }

word = []
for key in round_words.keys():
    word += [key]

final_words = ["jukebox", "keyhole", "knapsack", "espionage"]  # for the final

colorama.init(autoreset=True)
print(Fore.BLUE + Style.BRIGHT + "Welcome to wheel of luck! The rules are simple and we hope you can understand them.")
print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Rules:".center(75))
print(Fore.BLUE + Style.BRIGHT + "There are 4 rounds. Each of round has one hidden word or expression and you have to"
                                 "\ntry and find it,like hangman"
                                 "\nThe chances you have to find the word depend on how many letters the word has."
                                 "\nThe more you find the more money you earn and if you have passed at least two "
                                 "\nrounds out of 4 you play in the final"
                                 "\nThe final-difficulty is increased but for that reason you can reach a higher "
                                 "\namount of money.In the final, we will give you 3 letters of the WORD "
                                 "(not expression)"
                                 "\nand then you will have into 10 seconds to predict the word!If the prediction is"
                                 "\nright you multiply your money amount!If not,You will leave with your current amount"
                                 "\nYou have to follow the rules.We trust you!If you cheat,the game has no point and "
                                 "interest."
                                 "\nSo be careful and let's begin!")


# --------------------------------------------------------------------------------------------------------------------

def final():
    input(Fore.LIGHTWHITE_EX + Style.BRIGHT + "\nWelcome to the FINAL!If you are ready press any button!")
    global amount
    hidden_letters = []
    given = []
    hidden = final_words[random.randrange(4)]
    print("\nWORD OF FINAL SHAPED:")
    for abc in hidden:
        hidden_letters += [abc]  # list the hidden word's letters and then print ________ ...
        if abc.isalpha():
            print("_", end="")
    print('\nKNOWN LETTERS GIVEN:')
    for i in range(3):
        chosen = random.choice(hidden_letters)
        for elem in hidden_letters:
            if elem == chosen:
                hidden_letters.remove(chosen)
        given.append(chosen)
        time.sleep(2)
        print(chosen, end=" | ")
    print("\n")
    time.sleep(2)
    hidden_letters = []
    for abc in hidden:
        hidden_letters += [abc]  # list the hidden word's letters and then print ________ ...
        if abc == given[0] or abc == given[1] or abc == given[2]:
            print(abc, end="")
        else:
            print("_", end="")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\nNow you have 10 seconds to think and find the word!")
    for i in range(11):
        time.sleep(1)
        print(i, end=" , ")
    print("\nTIME IS OUT!")
    given_word = input("Give me your prediction or if you don't know press enter:").strip().lower()
    while not given_word.isalpha() and given_word != "":
        given_word = (input("Give me your prediction or if you don't know press enter,Only letters accepted:")
                      .strip().lower())
    if given_word == hidden:
        print(Fore.GREEN + Style.BRIGHT + "\nFINAL WIN! TOTAL AMOUNT EARNED:{amount}".format(amount=amount * 2))
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "\nLOOSE.That was an incredible round!You leave with:{}"
              .format(amount))
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Final word was:{}".format(hidden))
        quit()


def round_():
    global cnt, word, amount
    # for else statement , for the loose
    lost_chances = 0
    # for the win , for if statement
    hidden_letters = []
    already_guessed = []
    cnt += 1
    print()
    print(Fore.RED + Style.BRIGHT + "Round:{round}".format(round=cnt))
    hidden = word[random.randrange(0, len(word))]  # the hidden word
    # remove the current hidden word in order not to repeat in another round
    cur = round_words[hidden]
    word.remove(hidden)
    round_words.pop(hidden)
    # ---------------------------------------------------------------------
    print("HIDDEN WORD/EXPRESSION:")
    for abc in hidden:
        hidden_letters += [abc]  # list the hidden word's letters and then print ________ ...
        if abc.isalpha():
            print("_", end="")
        else:
            print(" ", end="")
    counter_for_win = 0
    for _ in hidden:
        counter_for_win += 1
    # for else statement , for the loose
    loose_at_ = len(hidden_letters) // 2
    # we are ready for the round --------------------------------------------------------------------
    while True:
        # inputs guess
        guess = input("\n\nTell me your guess-letter:").strip().lower()
        while guess == "" or not guess.isalpha() or guess in already_guessed:
            if guess in already_guessed:
                print("You've predicted already this letter!Try another one!")
            else:
                print("Oops wrong input. try again!")
            guess = input("\nTell me your guess-letter(carefully!):").strip().lower()
        # check if in else pass
        already_guessed.append(guess)
        if guess in hidden_letters:
            print("\nCongratulations!Letter '{}' exists! HIDDEN WORD SHAPED AS:".format(guess))
            # print the new formation,for example : ___t___s ...
            counter = 0
            for abc in hidden:
                if abc in already_guessed:
                    print(abc, end="")
                    counter += 1
                elif abc == " ":
                    print(" ", end="")
                    counter += 1

                else:
                    print("_", end="")
            if counter == counter_for_win:
                print(Fore.GREEN + Style.BRIGHT + "\n\nCONGRATS THE ROUND IS OVER . YOU WON!")
                amount += cur
                return 1
        else:
            lost_chances += 1
            if loose_at_ == lost_chances:
                print(Fore.RED + Style.BRIGHT + f"\n\nTHE ROUND IS OVER . YOU LOST!"
                                                f"\nHidden word/expression was: |{hidden}|")
                return 0
            else:
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\nWrong letter!Tries left:{tries}".format(
                    tries=loose_at_ - lost_chances))


def main():
    try:
        global amount
        j = 0
        for i in range(4):
            j += round_()
            if i == 2 and j == 0:
                print(Fore.RED + Style.BRIGHT + "\nGAME OVER. YOU ARE NOT ALLOWED TO CONTINUE!")
                quit()
        # check j==2
        if j >= 2:
            final()
        else:
            print(Fore.RED + Style.BRIGHT + "\nGAME OVER. YOU ARE NOT ALLOWED TO CONTINUE!")
            quit()
    except IndexError as e:
        print("ERROR. TRY AGAIN")
        print("\nonly for the programmer:Error{}:".format(e))
    except Exception as e:
        print("ERROR. TRY AGAIN")
        print("\nonly for the programmer:Error{}:".format(e))


if __name__ == "__main__":
    main()
