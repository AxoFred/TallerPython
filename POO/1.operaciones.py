from math import sqrt

class FGeneral:
    def __init__(self, valor1: float, valor2: float, valor3: float):
        self.a = valor1
        self.b = valor2
        self.c = valor3

    def FG(self) -> float:
        return (-self.b + sqrt((self.b * self.b) - ((4 * self.a) * (self.c)))) / (2 * self.a)

    def FG2(self) -> float:
        return (-self.b - sqrt((self.b * self.b) - ((4 * self.a) * (self.c)))) / (2 * self.a)

if __name__ == '__main__':
    resultado = FGeneral(6.0, 8.0, 2.0)
    print(resultado.FG())
    print(resultado.FG2)