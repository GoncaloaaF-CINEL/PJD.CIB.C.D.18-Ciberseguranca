from carro import Carro


c1 = Carro('Ford', 'Ka', 2019)
c2 = Carro('Chevrolet', 'Onix', 2020)
c3 = Carro('Ford', 'Mustang', 2025)

print(c1)
print(c2)
print(c3)

print(c1.marca)

c1.marca = 'Fiat'

c1.aclarar()
c2.aclarar()