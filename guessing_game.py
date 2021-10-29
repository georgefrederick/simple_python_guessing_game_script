#! /usr/bin/env python
import random
import time

def game():


    chances = 3
    attempts = 0
    computer_choice = random.randint(1,10)

    print('Pick a number between (1,10).\nYou only get 3 guesses.')
    time.sleep(2)
    try:
        while attempts < chances:
            my_answer = raw_input('My answer : ')
            my_answer = int(my_answer)

            if my_answer != computer_choice:
                attempts += 1
                print(str(chances-attempts)+' more chances left.')

            elif my_answer == computer_choice:
                attempts += 1
                print('Welldone, you guessed the right number after '+str(attempts)+' tries.')
                break
        else:
            print('You ran out of chances.\nThe winning number is '+str(computer_choice))
        time.sleep(2)

        print('Do you want to play again? Y/N:')

        decision = str(raw_input(' (y/n): ')).lower().strip()

        if decision[0] == 'y':
            game()

        elif decision[0] == 'n':
            print('It was nice playing with you. Goodbye :)')
            
    except ValueError: 
        print('Sorry, {} is not a valid selection.\nTry again?'.format(my_answer.upper()))
        time.sleep(1)
        decision = str(raw_input(' (y/n): ')).lower().strip()

        if decision[0] == 'y':
            game()

        elif decision[0] == 'n':
            print('It was nice playing with you. Goodbye :)')
                    

if __name__== '__main__':
    game()
