import random
fruits = ["Apple","Banana","Orange","Grapes","Mango","Strawberry","Pineapple","Watermelon","Blueberry","Kiwi","Melon","Pear","Avocado","Coconut","Lime","Cherry","Raspberry","Papaya","Pomegranate","Dragonfruit","Peach","Plum","Fig","Guava","Apricot","Nectarine","Grapefruit","Tangerine","Blackberry","Cranberry"]
fruit = random.choice(fruits).lower()
word_length = fruit.__len__()
# print('fruit --->> ',fruit)
run='y'
guess=''
while run=='y':
    guess_length = ''
    for i in fruit:
        if i not in guess:
            print(' _',end='')
        else:
            guess_length+=i
            print(f' {i}',end='')
    if guess_length.__len__()  == word_length:
        print('\nCongratulations! You have won the game!!')
        run='n'
        break
    print()
    g = input('Enter your guess : ')
    guess+=g
    # run=input(("\nDo you want to see another fruit? (yes/no): ").lower())