import random
num=random.randint(0,100)
print('Simple RNG\nBy MattCatt')
def game():
    print('Im thinking of a number between 0 and 100. Can you guess it? You have 10 attempts.')
    for i in range (10):
        try:
            guess=int(input())
        except:
            print('Enter a number.')
            guess=int(input())
        if guess == num:
            print('That is correct!')
            win=True
            break
        elif guess < num:
            print('Nice Try! Im thinking higher though.')
            print('You have',(9-i),'attempts left.')
        elif guess > num:
            print('Nice Try! Im thinking lower though.')
            print('You have',(9-i),'attempts left.')
    if win==True:
        print ('Good job! You discovered the answer in', (i+1), 'attempts.')
    else:
        print('Too bad. I was thinking of', num,'\n Better Luck Next Time!')
    print('Play Again? (Y)es | (N)o?')
    query=input()
    if query == 'Y' or query == 'y':
        game()
    elif query == 'N' or query == 'n':
        print('Goodbye!')
        SystemExit
    else:
        print('Unknown input. Restarting.')
        game()
game()