#-*- coding: utf8-*-

import sys
import platform

from parkin import Parking

class Menu():
    """ 
    Simula las opciones necesarias para gestionar los vehiculos
    """

    def __init__(self):
        self.parkin = Parking()
        self.opciones = {"1": self.add_vehiculo,
                         "2": self.mostrar_vehiculos,
                         "3": self.salir,
        }

    def Menu(self):
        """ Despliega el menu principal"""
        print("""
                   Menu de inicio
              1. Agregar nuevo vehiculo
              2. Mostrar Vehiculos en el parqueo
              3. Ver total a pagar
                """)


    def run(self):
        """ Método de entrada para la aplicación """
        while True:
            self.Menu()
            choise = input("Ingrese una opción: ")
            action = self.opciones.get(choise)

            if action:
                action()
            else:
                print("¡{0} no es una opción válida!".format(choise))

    def add_vehiculo(self):
        """ Permite enviar las caracteristicas de los vehiculos """
        marca = input("Ingrese la marca del vehiculo: ")
        tipo = input("Ingrese el tipo de vehiculo: ")
        placa = input("Ingrese la placa del vehiculo: ")
        modelo = input("Ingrese el modelo del vehiculo: ")
        self.parkin.new_vehiculo(placa, marca, modelo, tipo)

    def mostrar_vehiculos(self):
        """ Despliega los vehiculos """
        if not vehiculos:
            vehiculos = self.parkin.vehiculos

        for parking in vehiculos:
            print("Id: {0}\nplaca: {1}\ntipo: {2}\nmodelo: {3}\nhora de ingreso: {4}\nhora de salida: {5}\n estado: {6}"
                  .format())

    def salir(self):
        sys.exit(0)

        
if __name__ == "__main__":
    menu = Menu()
    menu.run()

    




