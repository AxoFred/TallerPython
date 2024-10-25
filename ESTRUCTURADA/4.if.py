if __name__ == '__name__':
    a = int(input("Teclea un numero: "))
    b = int(input("Teclea otro mas: "))
    c = int(input("Teclea uno mas: "))

    if a>b:
        if a>c:
            print("el mayor es :", a)
        else:
            print("el mayor es: ", c)
    elif b>c:
        print("el mayor es: ",b)
    else:
        print("el mayor es:",c)