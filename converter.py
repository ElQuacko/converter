class Operations: 
    result = ''
    hexDict = {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F'
    }

    def __init__(self, num):
        self.num = num

    def decimalToBinary(self):
        if self > 1:
            Operations.decimalToBinary(self // 2)
        print(self % 2, end = '')

    def decimalToOctal(self):
        if self > 7:
            Operations.decimalToOctal(self // 8)
        print(self % 8, end = '')

    def decimalToHex(self):
        if self > 15:
            Operations.decimalToHex(self // 16)
        modulo = self % 16
        if modulo > 9:
            print(Operations.hexDict[modulo], end = '')
        else:
            print(modulo, end = '')

def printResults(num):
    #DEC
    print("DEC:", num)
    #BIN
    print("BIN: ", end ='')
    Operations.decimalToBinary(num)
    print('')
    #OCT
    print("OCT: ", end ='')
    Operations.decimalToOctal(num)
    print('')
    #HEX
    print("HEX: ", end ='')
    Operations.decimalToHex(num)
    print('')

n = int(input("Enter number to change: "))

printResults(n)