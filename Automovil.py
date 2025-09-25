class Automovil:
        def __init__ (self, color, marca, aceleracion, velocidad, ruedas=4):
                self.ruedas = ruedas
                self.color = color
                self.marca = marca
                self.aceleracion = aceleracion
                self.velocidad = velocidad

        def __str__(self):
                return f"aceleracion: {self.aceleracion}, ruedas: {self.ruedas}"

        def acelera(self):
                self.velocidad += self.aceleracion
                return self.velocidad
        def frenar(self):
                self.velocidad -= self.aceleracion
                return self.velocidad

# aceleracion 20, velocidad 80
auto1 = Automovil("Rojo", "Ford", 20, 80)
print(auto1)
primeraAceleracion = auto1.aceleracion
auto1.aceleracion += 10 
print("aceleracion inicial ",primeraAceleracion,"nueva aceleracion ",auto1.aceleracion)

auto1.acelera()
print("Velocidad: ",auto1.velocidad,"km/h")
auto1.frenar()
print("Velocidad reducida: ",auto1.velocidad,"km/h")
