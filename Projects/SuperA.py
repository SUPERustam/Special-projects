# нахождение корней у многочлена
restore = []  # корни уравнения
a = [int(i) for i in input().split()]  # многочлен
w = len(a) - 1
a2 = []  # указатель на решения
s2 = 1
while len(a) != len(a2) and s2 < w:
    s = 0
    if a2 != []:
        a = a2
    p = []
    b1 = a[-1]
    q = []
    b2 = a[0]
    for i in range(1, int(abs(b1)) + 1):
        if b1 % i == 0:
            p.append(i)
    for i in range(1, int(abs(b2)) + 1):
        if b2 % i == 0:
            q.append(i)
            i //= -1
            q.append(i)
            i //= -1
    for i in p:
        for j in q:
            m = i / j
            c = a[0]
            cstore = []
            cstore.append(c)
            for t in range(1, len(a) - 1):  # схема Горнера
                c = a[t] + m * c
                cstore.append(c)
            c = a[-1] + m * c
            if c == 0 and s == 0:
                s += 1
                s2 += 1
                restore.append(str(i) + '/' + str(j))
                a2 = cstore
if len(a) == 3:  # решение квадратного трехчлена
    if a[1] ** 2 - 4 * a[0] * a[2] > 0:
        q1 = '(' + str(-a[1]) + ' + √ ' + str(a[1] ** 2 - 4 * a[0] * a[2]) + \
             ') / ' + str(2 * a[0])
        q2 = '(' + str(-a[1]) + ' - √ ' + str(a[1] ** 2 - 4 * a[0] * a[2]) + \
             ') / ' + str(2 * a[0])
        restore.append(q1)
        restore.append(q2)
    elif a[1] ** 2 - 4 * a[0] * a[2] == 0:
        q1 = str(-a[1]) + '/' + str(2 * a[0])
        restore.append(q1)
for i in restore:
    print(i, end='; ')
if len(restore) < w:
    for i in a:
        print(i, end='; ')
