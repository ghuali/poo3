class Romano:
    def __init__(self) -> None:
        self.romanos = {
            1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 400:"CD",500:"D",900:"CM",1000:"M"
        }
       
        
    
        
    
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
    def romanoEntero(self,romano):
        resultado = ""
        for valor,x in sorted(self.romanos.items(), reverse=True):
            while numero >= valor:
                resultado += x
                numero -= valor
        return resultado

if __name__ == "__main__":
    tests = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "XIV", "CXC", "MIM","XXX"]
    for test in tests:
        print(test, Romano.roman2int(test))
     
