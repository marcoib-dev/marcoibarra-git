class Animal:
    def __init__ (self, nombre):
        self.nombre = nombre
        
    def sonido(self):
        print("El animal hace un sonido")
        
class Perro(Animal):
    def sonido(self):
        print(f"{self.nombre} hace: Guau Guau")
        

class Gato(Animal):
    def sonido(self):
        print(f"{self.nombre} hace: Miau Miau")

class vaca(Animal):
    def sonido(self):
        print(f"{self.nombre} hace: Mooo Mooo")
        

#PRUEBAS

animales = [Perro("Perrito"), Gato("Gatito"), vaca("Vaca")]

animales[0].sonido()
animales[1].sonido()
animales[2].sonido()