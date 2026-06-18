# Integrantes:
# - Tatiana Villón Montenegro
# - Irina Alexandra Rivera Rivas
# - Karen Dayana Tomala Lino


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
