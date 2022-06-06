# declaramos la clase calculadora
class Calculadora:
    # declaramos el metodo __init__
    def __init__(self):
        self.num_A=int(input("Ingrese un número: "))
        self.num_B=int(input("Ingrese un otro número: "))

    # declaramos los metodos
    def suma(self):
        suma=self.num_A+self.num_B
        print("La suma de los números es: ",suma)

    def resta(self):
        resta=self.num_A-self.num_B
        print("La resta de los números es: ",resta)

    def multi(self):
        multi=self.num_A*self.num_B
        print("La multiplicación de los números es: ",multi)

    def divi(self):
        divi=self.num_A/self.num_B
        print("La división de los números es: ",divi)

# bloque de invocación
calculo=Calculadora()
calculo.suma()
calculo.resta()
calculo.multi()
calculo.divi()
        
