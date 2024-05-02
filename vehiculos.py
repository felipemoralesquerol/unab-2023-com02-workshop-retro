class Vehiculos:
    """
    Clase abstracta que se encarga de la gestión de los vehículos
    """
    def __init__(self, velocidad, color, capacidad) -> None:
        self.velocidad = velocidad
        self.color = color
        self.capacidad = capacidad

    def __str__(self) -> str:
        # TODO: Pasar a fstrings
        return 'Velocidad: ' + str(self.velocidad) + ' Color: ' + self.color + ' Capacidad: ' + str(self.capacidad)   
    
    def circular(self):
        """
        Método circular de Vehiculos
        """
        print('Circulando ...')