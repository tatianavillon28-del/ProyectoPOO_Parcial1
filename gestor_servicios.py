# Integrantes:
# -Villón Montenegro Tatiana Jazmin
# -Rivera Rivas  Irina Alexandra 
# -Tomala Lino Karen Dayana 


class GestorServicios:

    @staticmethod
    def generar_reporte(servicios):

        print("\n===== REPORTE DE SERVICIOS =====")

        for servicio in servicios:
            print(servicio.mostrar_info())

    @staticmethod
    def calcular_totales(servicios):

        total = 0

        for servicio in servicios:
            total += servicio.calcular_costo()

        return total
