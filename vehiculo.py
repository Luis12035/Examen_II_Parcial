#-*- coding: utf8 -*-

import datetime

class Vehiculo():
    """ Representa un vehiculo estacionado en el parqueo"""

    def __init__(self, placa, marca, modelo):
        """ Ddefinimos las caracteristicas del objeto """
        self.placaVehiculo = placa
        self.marcaVehiculo = marca
        self.modeloVehiculo = modelo
        self.horaIngreso = datetime.time.hour()
        self.estado = True

    
