# Integrantes:
# - Tatiana Villón Montenegro
# - Irina Alexandra Rivera Rivas
# - Karen Dayana Tomala Lino
#  Clase ExamenLaboratorio que hereda de Servicio ----

from servicio import Servicio


class ExamenLaboratorio(Servicio):

    def __init__(self, codigo, nombre, costo, tipo_examen):
        super().__init__(codigo, nombre, costo)
        self.tipo_examen = tipo_examen

    @property
    def tipo_examen(self):
        return self.__tipo_examen

    @tipo_examen.setter
    def tipo_examen(self, valor):
        if not valor.strip():
            raise ValueError("El tipo de examen no puede estar vacío")
        self.__tipo_examen = valor

    def calcular_costo(self):
        return self.costo + 10

    def mostrar_info(self):
        return (
            f"Examen: {self.nombre} | "
            f"Tipo: {self.tipo_examen} | "
            f"Total: ${self.calcular_costo():.2f}"
        )
