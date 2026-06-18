# Integrantes:
# -Villón Montenegro Tatiana Jazmin
# -Rivera Rivas  Irina Alexandra 
# -Tomala Lino Karen Dayana 

#####  Crear la superclase #------

class Servicio:

    def __init__(self, codigo, nombre, costo):
        self.codigo = codigo
        self.nombre = nombre
        self.costo = costo 

#  Encapsulamiento de atributos con validación ----

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        if valor <= 0:
            raise ValueError("Código inválido")
        self.__codigo = valor



    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError("Nombre vacío")
        self.__nombre = valor


    @property
    def costo(self):
        return self.__costo

    @costo.setter
    def costo(self, valor):
        if valor < 0:
            raise ValueError("Costo inválido")
        self.__costo = valor


#  Método para calcular el costo del servicio (puede ser sobrescrito por subclases) ----

    def calcular_costo(self):
        return self.costo

    def mostrar_info(self):
        return f"{self.nombre} - ${self.costo}"

    def __str__(self):
        return self.mostrar_info()
