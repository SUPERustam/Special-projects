import random


def choise1(answer1):  # выбор игрока 1
    global stopka
    global player1
    global strokes
    global score1
    if answer1 == '+':
        vybr = random.choice(stopka)
        del stopka[stopka.index(vybr)]
        player1.append(vybr[0])
        score1 += vybr[1]
        if answer2 != '-':
            strokes += 1
        print('Player1\'s carts:', *player1)
    elif answer1 == '-':
        strokes += 1
        print('Player1\'s pass')
    else:
        print('Error: change your answer')
        answer1 = input()
    return answer1


def choise2(answer2):  # выбор игрока 2
    global stopka
    global player2
    global strokes
    global score2
    if answer2 == '+':
        vybr = random.choice(stopka)
        del stopka[stopka.index(vybr)]
        player2.append(vybr[0])
        score2 += vybr[1]
        if answer1 != '-':
            strokes += 1
        print('Player2\'s carts:', *player2)
    elif answer2 == '-':
        strokes += 1
        print('Player2\'s pass')
    else:
        print('Error: change your answer')
        answer2 = input()
    return answer2


stopka = [(6, 6), (6, 6), (6, 6), (6, 6),
          (7, 7), (7, 7), (7, 7), (7, 7),
          (8, 8), (8, 8), (8, 8), (8, 8),
          (9, 9), (9, 9), (9, 9), (9, 9),
          (10, 10), (10, 10), (10, 10), (10, 10),
          ('Валет', 2), ('Валет', 2), ('Валет', 2), ('Валет', 2),
          ('Дама', 3), ('Дама', 3), ('Дама', 3), ('Дама', 3),
          ('Король', 4), ('Король', 4), ('Король', 4), ('Король', 4),
          ('Тус', 11), ('Тус', 11), ('Тус', 11), ('Тус', 11)]
player1 = []
player2 = []
answer1 = None
answer2 = None
score1 = 0
score2 = 0
strokes = 0

while answer1 != '-' or answer2 != '-':
    if strokes % 2 == 1 and answer2 != '-':
        answer2 = input()
        answer2 = choise2(answer2)
    elif strokes % 2 == 0 and answer1 != '-':
        answer1 = input()
        answer1 = choise1(answer1)
    if answer1 == '-' and answer2 == '-':
        break
print('          End Game')
print('Player1\'s carts:', *player1)
print('Player2\'s carts:', *player2)
if score2 <= 21 and score1 <= 21:
    if score1 < score2:
        print('Win Player2')
    elif score1 > score2:
        print('Win Player1')
    else:
        print('Draw')
elif score1 > 21 and score2 > 21:
    if score1 > score2:
        print('Win Player2')
    elif score1 < score2:
        print('Win Player1')
    else:
        print('Draw')
elif score1 <= 21 and score2 > 21:
    print('Win Player1')
elif score1 > 21 and score2 <= 21:
    print('Win Player2')
