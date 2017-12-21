number = 34
running = True
while running:
    guess = int(input('Enter an Integer : '))
    if guess == number:
        print('Congratulations, you guessed it')
        running = False
        # this causes the while loop to stop
    elif guess < number:
        print('No, it is little higher than that')
    else:
        print('No, it is little lower than that')
else:
    print('The while loop is over')
    # Do anything else you want to do here
print('Done')