from Automovil import Automovil


class AutomovilVolador(Automovil):
    def __init__(self, color, marca, aceleracion, velocidad, capacidad_combustible, altura_maxima, altura, ruedas=6, esta_volando=True):
        super().__init__(color, marca, aceleracion, velocidad, ruedas)
        # self.altura_maxima = altura_maxima  # Altura máxima de vuelo en metros
        self.capacidad_combustible = capacidad_combustible  # Capacidad de combustible en litros
        self.altura_maxima = altura_maxima
        self.altura = altura  # Altura actual en metros
        self.esta_volando = esta_volando  # Estado de vuelo (True si está volando, False si está en tierra)

    def volar(self, altura):
        if altura > self.altura_maxima:
            self.esta_volando = True
            return f"No se puede volar a {altura} metros. La altura maxima es {self.altura_maxima} metros."
        return f"El automovil esta volando a {altura} metros de altura."

    def aterrizar(self):
        self.esta_volando = False
        return "El automovil ha aterrizado exitosamente."
    
    def __str__(self):
        return f"Marca: {self.marca}, Color: {self.color}, Aceleracion: {self.aceleracion}, Velocidad: {self.velocidad}, capacidad_combustible: {self.capacidad_combustible}, altura_maxima: {self.altura_maxima}, altura: {self.altura}, ruedas: {self.ruedas}"
    

autoVolador1 = AutomovilVolador("Blanco", "Tesla", 30, 100, 50, 5000, 0)
print(autoVolador1.volar(3000))
print(autoVolador1.aterrizar())
print("Caracteristicas: ",autoVolador1)