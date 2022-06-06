# declaramos la clase alumno
class Alumno:
    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese su nombre completo: ")
        self.nota=float(input("Ingrese se nota: "))
        
    def mostrar(self):
        print("Nombre del alumno: ",self.nombre)
        print("Nota del alumno: ",self.nota) 

    # comprobacion si el alumno aprobo o reprobo
    def aprobacion(self):
        if self.nota >= 3:
            print("Felicidades, usted aprobó.")
        else:
            print("Lo sentimos, usted no aprobó.")

# bloque de invocación
sujeto=Alumno()
sujeto.mostrar()
sujeto.aprobacion()
        
