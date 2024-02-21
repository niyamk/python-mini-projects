import random,math
initial_range = int(input('Enter Initial range : '))
ending_range = int(input('Enter Ending range : '))

if ending_range < initial_range :
    print('please enter  a valid range')
else:
    bot = random.randint(initial_range,ending_range)
    # print(f'b - {bot}')
    max_no_guess = math.log2(ending_range-initial_range+1).__round__()
    print(f'you have {max_no_guess} guesses!!')
    while max_no_guess > 0:
        user = int(input('Enter number : '))
        # print(f'u - {user} , b - {bot}')
        if  user == bot:
            print('you guessed the word!!')
            break
        print('guessed too high') if user>bot else print('guessed too small') 
        print('number of guesses left => ',max_no_guess)
        max_no_guess-=1
    else :
        print('stopped')
    if max_no_guess == 0:
        print('you lost , number of guesses left -> ',max_no_guess) 