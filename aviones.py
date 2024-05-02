from vehiculosAereos import VehiculosAereos

class Aviones(VehiculosAereos):
   """
    Clase que se encarga de la gestión de los aviones
   """    
   def __init__(self, velocidad, color, capacidad, altitud) -> None:
      super().__init__(velocidad, color, capacidad)
      self.altitud = altitud

   def __str__(self) -> str:
      return super().__str__() + ' Altitud: ' + str(self.altitud)  

   def volar(self):
      """
      Método que se encarga de la información del vuelo
      """
      print("Avion volando")
       