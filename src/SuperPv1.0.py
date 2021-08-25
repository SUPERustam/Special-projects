a = int(input())
while bool(a) == True: 
    m = a % 10000 
    n = a // 10000 
    if m == 0: 
        m = ('0') 
    if m == 1: 
        m = ('(y \cdot z)') 
    if m == 10: 
        m = ('(y \cdot \overline{z})') 
    if m == 11: 
        m = ('y') 
    if m == 100: 
        m = ('(\overline{y} \ cdot z)') 
    if m == 101: 
        m = ('z') 
    if m == 110: 
        m = ('(y + z)') 
    if m == 111: 
        m = ('(y \\vee z)') 
    if m == 1000: 
        m = ('\overline{y \\vee z}')
    if m == 1001: 
        m = ('\overline{y + z}') 
    if m == 1010: 
        m = ('\overline{z}') 
    if m == 1011: 
        m = ('(y \vee \overline{z})') 
    if m == 1100: 
        m = ('\overline{y}') 
    if m == 1101: 
        m = ('(\overline{y} \\vee z)') 
    if m == 1110: 
        m = ('(\overline{y \cdot z})') 
    if m == 1111: 
        m = ('1') 
    if n == 0: 
        n = ('0') 
    if n == 1: 
        n = ('(y \cdot z)') 
    if n == 10: 
        n = ('(y \cdot \overline{z})') 
    if n == 11: 
        n = ('y') 
    if n == 100:
        n = ('(\overline{y} \ cdot z)') 
    if n == 101: 
        n = ('z') 
    if n == 110: 
        n = ('(y + z)')
    if n == 111: 
        n = ('(y \\vee z)')
    if n == 1000: 
        n = ('\overline{y \\vee z}')
    if n == 1001: 
        n = ('\overline{y + z}') 
    if n == 1010: 
        n = ('\overline{z}') 
    if n == 1011: 
        n = ('(y \\vee \overline{z})')
    if n == 1100: 
        n = ('\overline{y}') 
    if n == 1101: 
        n = ('(\overline{y} \\vee z)')
    if n == 1110: 
        n = ('(\overline{y \cdot z})') 
    if n == 1111: 
        n = ('1')       
    print('$$') 
    print('\overline{x} \cdot', n, ' \\vee x \cdot', m)
    print('$$')
    a = int(input()) 