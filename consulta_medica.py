# Integrantes:
# - Tatiana Villón Montenegro
# - Irina 
# - Karen Tomala

#  Clase ConsultaMedica que hereda de Servicio ----

from servicio import Servicio


class ConsultaMedica(Servicio):

    def __init__(self, codigo, nombre, costo, especialidad):
        super().__init__(codigo, nombre, costo)
        self.especialidad = especialidad

#  Encapsulamiento de atributos con validación ----

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, valor):
        if not valor.strip():
            raise ValueError("Especialidad vacía")
        self.__especialidad = valor

    def calcular_costo(self):
        return self.costo + 5
    

    def mostrar_info(self):
        return (
            f"Consulta: {self.nombre} "
            f"Especialidad: {self.especialidad} "
            f"Total: ${self.calcular_costo()}"
        )