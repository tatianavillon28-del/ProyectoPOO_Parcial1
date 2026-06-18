# Integrantes:
# - Tatiana Villón Montenegro
# - Irina Alexandra Rivera Rivas
# - Karen Dayana Tomala Lino

class Factura:

    def __init__(self, numero, paciente):
        self.numero = numero
        self.paciente = paciente

    def generar_factura(self):
        return (
            f"Factura N° {self.numero}\n"
            f"Paciente: {self.paciente.nombre}"
        )
