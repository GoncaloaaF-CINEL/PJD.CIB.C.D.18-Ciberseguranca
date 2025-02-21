from carro import Carro


c1 = Carro('Ford', 'Ka', 2019)
c2 = Carro('Chevrolet', 'Onix', 2020)
c3 = Carro('Ford', 'Mustang', 2025)

print(c1)
print(c2)
print(c3)

print(c1.marca)

c1.marca = 'Fiat'

c1.arrancar()
c1.acelerar(10)
c1.info()
c1.travar_para(5)
c1.info()
c1.parar()
c1.info()


"""
Classe Bola: Crie uma classe que modele uma bola: 
    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor
    

Classe Quadrado: Crie uma classe que modele um quadrado: 
    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;


"""