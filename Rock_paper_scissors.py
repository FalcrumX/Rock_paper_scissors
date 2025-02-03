import random
game = ['камень', 'ножницы', 'бумага']

print('Добро пожаловать в игру "камень, ножницы, бумага')

win = 0
loose = 0

while win != 3:
    choice = random.choice(game)
    word = input('Введите слово "камень", или "ножницы" или "бумага": ')
    if word == "камень" or word == "ножницы" or word == "бумага" :

        print('*Оппонент выбрал: ', choice)

        if (word == 'камень' and choice == 'ножницы') or (word == 'ножницы' and choice == 'бумага') or (word == 'бумага' and choice == 'камень'):
            win +=1
            print('Этот раунд Вы выиграли!')
        elif (word == 'камень' and choice == 'камень') or (word == 'ножницы' and choice == 'ножницы') or (word == 'бумага' and choice == 'бумага'):
            print('-Этот раунд закончился ничьей!')
        else:
            loose += 1
            print('-Этот раунд Вы проиграли!')

    else:
        print('ВНИМАНИЕ! Ваше слово введено некорректно!')
        word = input('Введите слово "камень", или "ножницы" или "бумага": ')
        print('*Оппонент выбрал: ', choice)

        if (word == 'камень' and choice == 'ножницы') or (word == 'ножницы' and choice == 'бумага') or (word == 'бумага' and choice == 'камень'):
            win +=1
            print('Этот раунд Вы выиграли!')
        elif (word == 'камень' and choice == 'камень') or (word == 'ножницы' and choice == 'ножницы') or (word == 'бумага' and choice == 'бумага'):
            print('-Этот раунд закончился ничьей!')
        else:
            loose += 1
            print('-Этот раунд Вы проиграли!')

    if win == 3 and win > loose:
        print('   ***Ура! Победа!***')
    elif loose == 3 and loose > win:
        print('   ***Очень жаль, но Вы проиграли...***')
        break
    else:
        continue