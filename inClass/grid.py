"""This the module I made for making the grid

it has two functions, addToString(), and grid()

>>> addToString(' ', ' ')
'  '
>>> grid(1, 1, 1)
+-+\n| |\n+-+
"""

def addToString(s1, s2):
    """Function takes in grid string, and adds string s to it"""
    s1 = s1 + s2
    return s1
def grid(nRows, nCols, sideLength):
    """Function takes in number of rows (nRows), number of columns (nCols), and
    the side length of a cell (sideLength)
    and prints out a grid with those specifications"""

    junctionString = '+'
    structureString = '|'
    for i in range(nCols):
        junctionString = junctionString + '-'*sideLength + '+'
        structureString = structureString + ' '*sideLength + '|'

    gridString = ''
    for i in range(nRows):
        gridString = addToString(gridString, junctionString+'\n')
        for i in range(sideLength):
            gridString = addToString(gridString, structureString+'\n')
        gridString = addToString(gridString, junctionString)
    print(gridString)
