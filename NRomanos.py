class Romano:
    def __init__(self, roman):
        self.roman = roman

        
romanos = {'I': 1, 'V': 5, 'X': 10,
               'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman2int(romval):
    total = 0
    prev = 0
    for letra in romval[::-1]:
        valor = romanos[letra]
        total += valor if valor >= prev else -valor
        prev = valor

    return total


if __name__ == "__main__":
    tests = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "XIV", "CXC", "MIM"]
    for test in tests:
        print(test, roman2int(test))