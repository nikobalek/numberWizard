print('choose a number between 1 and 1000! and I will guess it bitch')


max = 1000
min = 1
guess = 500
preGuess = 500

uinput = input(f'is it upper or lower than {guess}')

while True:

    if uinput == 'l':
        max = guess
        preGuess = guess
        guess = int((max + min) / 2)
        if preGuess == guess + 1:
            print(f"found it its {guess}")
            break
    elif uinput == 'u':
        min = guess
        preGuess = guess
        guess = int((max + min) / 2)
        if preGuess == guess - 1:
            print(f"found it its {guess}")
            break
    elif uinput == 'y':
        print('yeah mother fucker I told I would guess it bitch')
        break
    else:
        print('enter wather l or u you stupid bitch')

    uinput = input(f"is your number lower or upper or it is {guess}")
