number = 17
guess = int(input('Enter an Integer : '))
if guess == number:
    print('Congratulations, you guessed it.')
    # New block start here
    print('but you do not win any prizes!')
    # New block end here
elif guess < number:
    print('No, it is little higher than that')
    # Another block
    # You can do whatever you want in this block...
else:
    print('No, it is little lower than that')
    # You most have guess > number to reach here
print('Done')
# The last statement always executed, after if statement executed
