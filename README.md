# Proyecto Primer Parcial - Sistema de Gestión de Servicios de Clínica

## Integrantes

* Villón Montenegro Tatiana Jazmin
* Rivera Rivas Irina Alexandra
* Tomala Lino Karen Dayana

## Descripción

Este proyecto fue desarrollado utilizando Programación Orientada a Objetos (POO) en Python.

El sistema permite gestionar servicios médicos de una clínica, incluyendo consultas médicas, exámenes de laboratorio, pacientes y facturación.

## Clases del proyecto

### Servicio

Clase base que contiene los atributos y métodos comunes para todos los servicios.

### ConsultaMedica

Hereda de Servicio y representa una consulta médica con una especialidad determinada.

### ExamenLaboratorio

Hereda de Servicio y representa un examen de laboratorio.

### Paciente

Almacena la información del paciente.

### Factura

Genera la información de facturación del paciente.

### GestorServicios

Permite generar reportes y calcular los costos totales de los servicios.

## Conceptos POO aplicados

### Encapsulamiento

Se utilizaron atributos privados mediante `__atributo` y acceso controlado mediante `@property` y `@setter`, incluyendo validaciones de datos.

### Herencia

Las clases `ConsultaMedica` y `ExamenLaboratorio` heredan de la clase base `Servicio`.

### Polimorfismo

Se implementó mediante los métodos:

* `generar_reporte()`
* `calcular_totales()`

Estos métodos trabajan con listas de objetos de diferentes tipos de servicios sin necesidad de identificar su tipo.

## Instrucciones de ejecución

1. Abrir el proyecto en Visual Studio Code.
2. Ejecutar el archivo `main.py`.
3. Visualizar los resultados en la consola.

## Evidencia de ejecución

![Evidencia de ejecución](Captura%20%20.png)

## Video

Video explicativo
