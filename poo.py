## crear una clase llamada vehículo capaz de procesar la información básica de los autos en una concesionaria. Deberá tener constructor y los atributos del vehículo serán: patente, marca, modelo, kilometraje. Crear métodos (de acceso) getter y (de modificación) setter. Mostar por pantalla al menos un atributo y modificar el kilometraje. 
class Vehiculo:
  def __init__(self, patente, marca, modelo, kilometraje):
    self.patente = patente
    self.marca = marca
    self.modelo = modelo
    self.kilometraje = kilometraje

def get_patente(self):
  return self.patente

def set_kilometraje(self, nuevo_kilometraje):
  self.kilometraje = nuevo_kilometraje
  print("El kilometraje ha sido actualizado. ")

auto1 = Vehiculo("ABC123", "Toyota". "Corolla", 50000)
print("Patente del vehiculo: ", auto1.get_patente())
print("Kilometraje actual: ", auto1.kilometraje)
auto1.set_kilometraje(55000)
print("Nuevo kilometraje: ", auto1.kilometraje)
