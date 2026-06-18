# Integrantes:
# - Tatiana Villón Montenegro
# - Irina Alexandra Rivera Rivas
# - Karen Dayana Tomala Lino
#  main.py  Punto de entrada del programa ----


from consulta_medica import ConsultaMedica
from examen_laboratorio import ExamenLaboratorio
from paciente import Paciente
from factura import Factura
from gestor_servicios import GestorServicios


# Paciente
paciente = Paciente(
    "0958741236",
    "Tatiana Villon",
    37
)

# Consultas
consulta1 = ConsultaMedica(
    1,
    "Consulta General",
    25,
    "Medicina General"
)

consulta2 = ConsultaMedica(
    2,
    "Consulta Ginecológica",
    30,
    "Ginecología"
)

# Exámenes
examen1 = ExamenLaboratorio(
    3,
    "Biometría",
    20,
    "Sangre"
)

examen2 = ExamenLaboratorio(
    4,
    "Examen de Orina",
    15,
    "Orina"
)

# Lista polimórfica
servicios = [
    consulta1,
    consulta2,
    examen1,
    examen2
]

# Método polimórfico 1
GestorServicios.generar_reporte(servicios)

# Método polimórfico 2
print("\n===== TOTAL GENERAL =====")
print(
    f"${GestorServicios.calcular_totales(servicios):.2f}"
)

# Uso de __str__
print("\n===== PACIENTE =====")
print(paciente)

# Factura
factura = Factura(
    1001,
    paciente
)

print("\n===== FACTURA =====")
print(factura.generar_factura())


