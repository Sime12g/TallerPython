from math import sqrt


class formula:

    def __init__(self, valor1, valor2, valor3):
        self.a = valor1
        self.b = valor2
        self.c = valor3
    def mult(self):
        return self.a*self.b*4
    def cuad(self):
        return self.b*self.b
    def resta(self):
        return self.cuad() - self.mult()
    def raiz(self):
        return sqrt(self.resta())
    def prod(self):
        return self.a*2
    def x1(self):
        return -self.b+self.raiz()/self.prod()
        self.x1()
    def x2(self):
        return -self.b + self.raiz() / self.prod()
        self.x2()

if __name__ == '__main__':
    resultado = formula(2, 8, 3)
    print(f"x1 = {resultado.x1()},x2 = {resultado.x2()}")