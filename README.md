# Proyecto Primer Parcial POO
Proyecto Primer Parcial - Sistema de Gestión de Servicios de Clínica
Integrantes
Villón Montenegro Tatiana Jazmin
Rivera Rivas Irina Alexandra
Tomala Lino Karen Dayana

### Descripción  

Este proyecto fue desarrollado utilizando Programación Orientada a Objetos (POO) en Python.

El sistema permite gestionar servicios médicos de una clínica, incluyendo consultas médicas y exámenes de laboratorio.

## Clases del proyecto

### Servicio

Clase base que contiene los atributos y métodos comunes para todos los servicios.

### ConsultaMedica

Hereda de Servicio y representa una consulta médica con especialidad.

### ExamenLaboratorio

Hereda de Servicio y representa un examen de laboratorio.

### Paciente

Almacena la información del paciente.

### Factura

Genera la información de facturación del paciente.

### GestorServicios

Permite generar reportes y calcular totales de los servicios.

## Conceptos POO aplicados

### Encapsulamiento

Se utilizaron atributos privados mediante `__atributo` y acceso controlado con `@property` y `@setter`.

### Herencia

Las clases `ConsultaMedica` y `ExamenLaboratorio` heredan de la clase `Servicio`.

### Polimorfismo

Se implementó mediante los métodos:

* generar_reporte()
* calcular_totales()

Los cuales trabajan con listas de objetos de diferentes tipos de servicios.

## Instrucciones de ejecución

1. Abrir el proyecto en Visual Studio Code.
2. Ejecutar el archivo `main.py`.
3. Visualizar los resultados en consola.

## Evidencia de ejecución
![alt text](<Captura  -1.png>)


## Video

Video explicativo.

