import random

num = random.randint(1, 100)

print("ДОБРО ПОЖАЛОВАТЬ В ИГРУ УГАДАЙ ЧИСЛО!")
print("Я загадал число от 1 до 100")
print("Если Ваша отгадка дальше чем на 10 от моего числа, то я скажу вам ХОЛОДНО")
print("Если Ваша отгадка ближе чем на 10 от моего числа, то я скажу вам ТЕПЛО")
print("Если Ваша отгадка дальше чем предыдущая отгадка, то я скажу вам ХОЛОДНЕЕ")
print("Если Ваша отгадка ближе чем предыдущая отгадка, то я скажу вам ТЕПЛЕЕ")
print("НАЧНЁМ ИГРУ!")

old_clue = [0]

while True:

    player = int(input('Ваше число: '))

    if player < 1 or player > 100:
        print('ВНЕ ДИАПАЗОНА! Попробуйте еще: ')
        continue

    if num == player:
        print(f'ВЫ УГАДАЛИ, ЭТО ЗАНЯЛО {len(old_clue)} ПОПЫТОК!')
        break 

    old_clue.append(player)
    
    if old_clue[-2]:
        if abs(num - player) < abs(num - old_clue[-2]):
            print('ТЕПЛЕЕ')
        else:
            print('ХОЛОДНЕЕ')
    else:
        if abs(num - player) <= 10:
            print('ТЕПЛО!')
        else:
            print('ХОЛОДНО')