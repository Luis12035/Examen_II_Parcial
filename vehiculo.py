#-*- coding: utf8 -*-

from datetime import datetime, timedelta
from random import randint


vehiculo_id = 0

class Vehiculo():
    """ Representa un vehiculo estacionado en el parqueo"""


    def __init__(self, placa, marca, modelo, tipo):
        """ Ddefinimos las caracteristicas del objeto """
        self.placaVehiculo = placa
        self.marcaVehiculo = marca
        self.modeloVehiculo = modelo
        self.tipoVehiculo = tipo
        global vehiculo_id
        vehiculo_id += 1
        self.idVehiculo = vehiculo_id
        self.horaIngreso = datetime.now()
        self.horaSalida = timedelta(randint(1,5))
        self.estado = True


    
