from enum import Enum, unique, auto


class Esempio(Enum):
    PRIMO = 1
    SECONDO = 2
    ALTRI = 1


# print(Esempio.PRIMO == Esempio.ALTRI)
# print(Esempio.PRIMO.value == Esempio.ALTRI.value)


@unique
class Pianeta(Enum):
    MERCURIO = 10
    VENERE = 20
    TERRA = auto()
    MARTE = auto()
    GIOVE = auto(80)
    SATURNO = auto()
    URANO = auto()
    NETTUNO = auto()


for pianeta in Pianeta:
    print(f"{pianeta.name} ha il valore {pianeta.value}")
