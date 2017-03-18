print "Welcome to Guess a secret number!\n"

from random import randint

numbers = range(1,101)

def main():
    while True:
        try:
            random_number = randint(1, 101)
            guess = int(raw_input("Guess a secret number between 1 and 100?\n>> "))
            if check_guess1(guess, random_number):
                break

        except ValueError:
            print "\nOops that was no number! Try again!\n"
            continue

    print "END"
    print "_____________________"


def check_guess1(guess, random_number):
    if guess == random_number:
        print "\nNice one you have won!!\n"
        return True
    else:
        print "\nSorry you lost. Try again!\n"
        return False




if __name__ == '__main__':
    main()


