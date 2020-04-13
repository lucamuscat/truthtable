


def createSegment(column, bits):
    index = column - 1
    size = 2**index
    temp = []
    for i in range(bits // (2**column)):
        for j in range(size):
            temp.append(0)
        for j in range(size):
            temp.append(1)
    return temp

def createColumns(columns):
    """
    @param columns: Number of columns you want your truth table to have.
    """
    bits = 2**columns
    temp = tuple(createSegment(i, bits) for i in range(1, 7))
    return temp

def printTruthTableBigEndianess(columns):
    temp = createColumns(columns)
    for i in list(zip(*temp[::-1])):
        print(i)


def printTruthTableLittleEndianess(columns):
    temp = createColumns(columns)
    for i in list(zip(*temp)):
        print(i)

printTruthTableBigEndianess(6)
printTruthTableLittleEndianess(6)



