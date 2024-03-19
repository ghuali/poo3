class Romano:
    def __init__(self, roman):
        self.roman = roman

        

    @staticmethod
    def roman2int(romval):
        romanos = {'I': 1, 'V': 5, 'X': 10,
               'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0
        for letra in romval[::-1]:
            valor = romanos[letra]
            total += valor if valor >= prev else -valor
            prev = valor

        return total

def int2roman(valrom):
    total = ""
    listanum = 0
    
    while valrom > 0:
        div = valrom // romanos[listanum]
        valrom %= romanos[listanum]
        total += romanos[listanum] * div
        listanum += 1


    return total

if __name__ == "__main__":
    tests = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "XIV", "CXC", "MIM","XXX"]
    for test in tests:
        print(test, Romano.roman2int(test))
    testeo = [12,5,20,4]
    for testt in testeo:
        print(testt,int2roman(testt))