import random
l = ['rainbow', 'butterfly', 'castle', 'pirate', 'ghost', 'music', 'beach', 'mountain', 'forest', 'rainbow', 'puzzle', 'popcorn', 'rainbow', 'umbrella', 'sandwich', 'rainbow', 'camera', 'sunglasses', 'rainbow', 'microphone', 'paintbrush', 'rainbow', 'telescope', 'compass', 'rainbow']
word= random.choice(l)
# word = 'dog'
guess = ''
attempts = len(word)*2
print('GAME BEGINS....')
while attempts>0:
    found = ''
    for i in word:
        if i not in guess : 
            print('-') 
        else :
            found+=i
            print(f'{i}')
            if len(found)==len(word):
                print('game over! you won!')
                attempts = 0
                break
    if attempts>0:
        print('number of tries left - > ',attempts)
        g = input("enter  a letter: ").lower() 
        guess += g
    attempts-=1
else:
    print('You Lost!!!')
    # run = input('Enter y to run : ')