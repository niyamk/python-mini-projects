import random
l = ['rocks','papers','scissors']
print('choose from ',l)
l2 = l.copy()
l2.insert(0,l2.pop())
run = 'y'
while run.lower() == 'y':
    user = input('Enter : ')
    bot = random.choice(l)
    print(f'user -> {user} , bot -> {bot}')
    if user == bot:
        print('draw')
    elif l.index(user)==l2.index(bot):
        print('user wins')
    else:
        print('bot wins')
    run = input('Enter y to continue : ')
