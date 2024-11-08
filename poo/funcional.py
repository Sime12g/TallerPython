import math

if __name__ == '__main__':

        potencia = lambda x:x**2
        print(f"la potencia es {potencia(7)}")

        suma = lambda x,y:x+y
        print(f"La suma es {suma(2,3)}")

        X1 = lambda a,b,c:(-b + math.sqrt(b**2 - 4*a*c)/2*a)
        X2 = lambda a,b,c:(-b - math.sqrt(b**2 - 4*a*c)/2*a)
        print(f"El resultado es {X1(2,5,1)} y {X2(2,5,1)}")
