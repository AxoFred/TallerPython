if __name__ == '__main__':
    nom = (input("proporciona un nombre: "))
    fecha = ""
    match nom:
        case "karen": fecha = "6 de marzo"
        case "ana": fecha = "1 de diciembre"
        case "fredy": fecha = "7 de marzo"
        case "karina": fecha = "23 de marzo"
        case "victor": fecha = "29 de mayo"
        case _: fecha = "fecha no valida"
    print(f"la fecha de cumpleaños es: {fecha}")