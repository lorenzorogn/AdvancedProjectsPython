from enum import Enum


class ColorePrimario(Enum):
    ROSSO = 1
    VERDE = 2
    BLU = 3


class PuntoCardinale(Enum):
    NORD = "N"
    SUD = "S"
    EST = "E"
    OVEST = "O"


for direzione in PuntoCardinale:
    print(f"Nome: {direzione.name},"
          f"Valore: {direzione.value}")

direzione_scelta = PuntoCardinale.NORD
if direzione_scelta == PuntoCardinale.NORD:
    print("Stai andando verso nord!")


