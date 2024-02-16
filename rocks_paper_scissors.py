import random
l = ['rocks','papers','scissors']
  # ['scissors','rocks','papers']
# l2 = l.insert(0,l.pop(1)
l2 = l.copy()
l2.insert(0,l2.pop())
run = 'y'
while run == 'y':
    user = input('Enter : ')
    bot = random.choice(l)
    print(f'user -> {user} , bot -> {bot}')
    if user == bot:
        print('draw')
    elif l.index(user)==l2.index(bot):
        print('bot wins')
    else:
        print('user wins')
# print(f'{l} {l2}')