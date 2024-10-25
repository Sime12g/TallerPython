if __name__ == '__main__':
    a=int(input("Teclee un numero: "))
    b=int(input("Teclee otro numero: "))
    c=int(input("Teclee otro numero"))

    if a>b:
        if a>c:
            print(f"el mayor es {a}")
        else:
            print(f"El mayor es {c}")
    elif b>c:
        print(f"El mayor es la {b}")
    else:
        print(f"El mayor es la {c}")


