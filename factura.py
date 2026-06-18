# Integrantes:
# - Villón Montenegro Tatiana Jazmin
# - Rivera Rivas Irina Alexandra
# - Tomala Lino Karen Dayana

class Factura:

    def __init__(self, numero, paciente):
        self.numero = numero
        self.paciente = paciente

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valor):
        if valor <= 0:
            raise ValueError("Número de factura inválido")
        self.__numero = valor

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, valor):
        if valor is None:
            raise ValueError("Debe asignar un paciente")
        self.__paciente = valor

    def generar_factura(self):
        return (
            f"Factura N° {self.numero}\n"
            f"Paciente: {self.paciente.nombre}"
        )

    def __str__(self):
        return self.generar_factura() 
