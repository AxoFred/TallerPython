import math
if __name__ == '__main__':

    #lambda
    Suma = lambda x,y:x+y
    print(f"la suma es: {Suma(2,6)}")

    Potencia = lambda x:x**2
    print(f"la potencia es: {Potencia(9)}")

    X1 = lambda a, b, c: (-b + math.sqrt(b ** 2) * (4 * a * c)) / 2 * a
    X2 = lambda a, b, c: (-b - math.sqrt(b ** 2) * (4 * a * c)) / 2 * a

    print(f"la FormulaG {X1(2,4,8)}")
    print(f"la FormulaG {X1(6, 8, 10)}")
