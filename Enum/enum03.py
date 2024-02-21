from enum import Enum


class Stagione(Enum):
    PRIMAVERA = 1
    ESTATE = 2
    AUTUNNO = 3
    INVERNO = 4

    def descrizione(self):
        return {
            Stagione.PRIMAVERA: "Il tempo si riscalda",
            Stagione.ESTATE: "Tempo di spiaggia",
            Stagione.AUTUNNO: "Le foglie cadono",
            Stagione.INVERNO: "Neve e ghiaccio"
        }[self]

    @property
    def fa_caldo(self):
        return self in {Stagione.PRIMAVERA, Stagione.ESTATE}
    

stagione_corrente = Stagione.ESTATE
print(stagione_corrente.descrizione())
print(stagione_corrente.fa_caldo)

