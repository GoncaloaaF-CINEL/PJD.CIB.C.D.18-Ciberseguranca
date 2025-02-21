from dataclasses import dataclass

"""
Classe Bola: Crie uma classe que modele uma bola: 
    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor

"""


@dataclass
class Bola:
    cor: str
    circunferencia: float
    material: str

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print(self.cor)






"""
Classe Quadrado: Crie uma classe que modele um quadrado: 
    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;


"""