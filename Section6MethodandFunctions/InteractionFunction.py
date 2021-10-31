from random import shuffle
example = [1, 2, 3, 4, 5, 6, 7]

result = shuffle(example)

# game


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:  # chekc if the number is in 0,1,2
        guess = input('Pick a number: 0,1,2\n')
    return int(guess)


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct')
    else:
        print("Wrong")
        print(mylist)


# Initial list
mylist = ['', 'O', '']
# shuffle list
mixlist = shuffle_list(mylist)
# User guess
user = player_guess()
# Check user guess
check_guess(mylist, user)
