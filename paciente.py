# Integrantes:
# -Villón Montenegro Tatiana Jazmin
# -Rivera Rivas  Irina Alexandra 
# -Tomala Lino Karen Dayana 

class Paciente:

    def __init__(self, cedula, nombre, edad):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, valor):
        if not valor.strip():
            raise ValueError("La cédula no puede estar vacía")
        self.__cedula = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self.__nombre = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if valor <= 0:
            raise ValueError("Edad inválida")
        self.__edad = valor

    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"
