import random

#tracking wins
user_wins = 0
comp_wins = 0

while True:

    lose = ('Haha, you got beat by 50 lines of code')
    win = ('You won this round')

    user_choice = input('Choose rock, paper or scissors: \n')

    if user_choice in ['Rock', 'rock', 'R', 'r']:
        user_choice = 'r'
    elif user_choice in ['Paper', 'paper', 'P', 'p']:
        user_choice = 'p'
    elif user_choice in ['Scissors', 'scissors', 'S', 's']:
        user_choice = 's'
    else:
        print('Thats not rock paper or scissors')
        exit()

    comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice = 'r'
    elif comp_choice == 2:
        comp_choice = 'p'
    else:
        comp_choice = 's'

    #comparing user to comp choice
    if user_choice == comp_choice:
        print('Issa draw')

    if user_choice == 'r' and comp_choice == 'p':
        comp_wins = comp_wins + 1
        print(lose)
    if user_choice == 'p' and comp_choice == 's':
        comp_wins = comp_wins + 1
        print(lose)
    if user_choice == 's' and comp_choice == 'r':
        comp_wins = comp_wins + 1
        print(lose)

    if user_choice == 'r' and comp_choice == 's':
        user_wins = user_wins + 1
        print(win)
    if user_choice == 's' and comp_choice == 'p':
        user_wins = user_wins + 1
        print(win)
    if user_choice == 'p' and comp_choice == 'r':
        user_wins = user_wins + 1
        print(win)


    print('Your wins', user_wins)
    print('Computer wins', comp_wins)

    cont = input('Would you like another round? \n')

    if cont in ['No', 'no', 'N', 'n']:
        print('Thanks for playing, goodbye')
        exit()
    else:
        continue
