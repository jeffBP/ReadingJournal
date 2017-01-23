def right_justify(s):
    """ Function that takes in String s and prints a number of spaces
    so that the string ends on column 80"""
    justification = ' '*(80-len(s))  #calculate spaces
    print justification + s

def print_strut(n):
    print '+' + ('-' * n) + '+' + ('-'*n) + '+'


def print_interior(n):
    print '|' + (' ' * n) + '|' + (' '*n) + '|'

def print_box():
    print_strut(4)
    print_interior(4)
    print_interior(4)
    print_interior(4)
    print_interior(4)
    print_strut(4)
    print_interior(4)
    print_interior(4)
    print_interior(4)
    print_interior(4)
    print_strut(4)



def print_small_box():
    top = '+' + '-'*2 + '+' + '\n'
    middle = '|' + ' '*2 + '|' + '\n'

    print top, middle * 2, top


def check_fermat(a, b, c, n):
    side1 = a**n + b**n
    side2 = c**n
    if side1 == side2:
        print 'Holy smokes, Fermat was wrong!'
    else:
        print 'No, that doesn\'t work'

def fermat_input():
    int1 = input('First number: ')
    int2 = input('Second number: ')
    int3 = input('Third number: ')
    power = input('Power: ')

    int1 = int(int1)
    int2 = int(int2)
    int3 = int(int3)
    power = int(power)

    check_fermat(int1, int2, int3, power)


def is_triangle(a, b, c):
    check1 = (a+b) > c
    check2 = (b+c) > a
    check3 = (a+c) > b
    if check1 and check2 and check3:
        print 'It is a triangle'
    else:
        print 'It is not a triangle'


def triangle_input():
    int1 = input('First length: ')
    int2 = input('Second length: ')
    int3 = input('Third length: ')

    int1 = int(int1)
    int2 = int(int2)
    int3 = int(int3)

    is_triangle(int1, int2, int3)


triangle_input()
