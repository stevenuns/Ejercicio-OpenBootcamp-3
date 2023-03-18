# Creamos la clase Persona con las variables comunes a todas las personas
class Persona:
    def __init__(self, edad, nombre, telefono):
        self.edad = edad
        self.nombre = nombre
        self.telefono = telefono

# Creamos la clase Cliente que hereda de Persona
class Cliente(Persona):
    def __init__(self, edad, nombre, telefono, credito):
        super().__init__(edad, nombre, telefono)
        self.credito = credito

# Creamos un objeto de la clase Cliente y mostramos sus propiedades
cliente1 = Cliente(30, "Juan", "123456789", 5000)
print("Cliente 1:")
print("Edad:", cliente1.edad)
print("Nombre:", cliente1.nombre)
print("Teléfono:", cliente1.telefono)
print("Crédito:", cliente1.credito)

# Creamos la clase Trabajador que hereda de Persona
class Trabajador(Persona):
    def __init__(self, edad, nombre, telefono, salario):
        super().__init__(edad, nombre, telefono)
        self.salario = salario

# Creamos un objeto de la clase Trabajador y mostramos sus propiedades
trabajador1 = Trabajador(25, "María", "987654321", 1500)
print("Trabajador 1:")
print("Edad:", trabajador1.edad)
print("Nombre:", trabajador1.nombre)
print("Teléfono:", trabajador1.telefono)
print("Salario:", trabajador1.salario)
