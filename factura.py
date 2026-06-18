# Integrantes:
# -Villón Montenegro Tatiana Jazmin
# -Rivera Rivas  Irina Alexandra 
# -Tomala Lino Karen Dayana 

class Factura:

    def __init__(self, numero, paciente):
        self.numero = numero
        self.paciente = paciente

    def generar_factura(self):
        return (
            f"Factura N° {self.numero}\n"
            f"Paciente: {self.paciente.nombre}"
        )
