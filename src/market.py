import random
print('Вы находитесь на рынке. Вы можете пойти в 1, 2, или \
в 3 лавку. Введите одну цифру для выбора.')
dead = ['Вас убили(', 'Выбирете, что будете покупать: "Помидоры" или \
"Апельсины". Введите одно из слов в кавычках для выбора.']
r1 = random.choice(dead)
q = input()
if (q == '1' or q == '2') and 'Выбирете, что будете покупать: "Помидоры" или \
"Апельсины". Введите одно из слов в кавычках для выбора.' in r1:
    print(r1)
    w = input()
    while w:
        if "Помидоры" in w:
            print('Спасибо за покупку!')
            break
        elif 'Апельсины' in w:
            print('Нет в продаже!')
            print('Вас убили(')
            break
        else:
            print('Ошибка')
elif (q == '1' or q == '2') and 'Вас убили(' in r1:
    print('Вас убили(')
    print('GAME OVER(')
elif q == 3:
    print('Молодец! Ты нашёл выход из базара. Напиши "ДА", если хочешь получить\
    подарок!')
    a = input()
    if 'ДА' in a:
        print('Вас убили((((')
        print("GAME OVER)")
    else:
        print('Я Вас не понимаю, Хозяин')
else:
    print('Я Вас не понимаю, Хозяин')
