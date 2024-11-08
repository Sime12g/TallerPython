class formulagen:
    def __init__(self, valor1, valor2, valor3):
        # self.metodo1()
        self.nombre = "Xayli"
        self.correo = "xayli2018"
        self.a = 248

    def datos (self):
        print("Nombre: ",self.nombre)
        self.materia()

    def materia(self):
        print("Administracion")

if __name__ == '__main__':
    print("xAYLI")
    obj=formulagen(2,8,3)
    obj.datos()