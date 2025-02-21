from carro import Carro


c2 = Carro('Chevrolet', 'Onix', 2020)
c3 = Carro('Ford', 'Mustang', 2025)
ford1 = Carro('Ford', 'Ka', 2019)
ford2 = Carro('Ford', 'Fiesta', 2020)
ford3 = Carro('Ford', 'Focus', 2021)
ford4 = Carro('Ford', 'Mustang', 2022)
ford5 = Carro('Ford', 'Explorer', 2023)

bmw1 = Carro('BMW', 'X5', 2021)
bmw2 = Carro('BMW', 'M3', 2022)



lista_carros = [c2, c3, ford1, ford2, ford3, ford4, ford5, bmw1, bmw2]

for c in lista_carros:
    print(c.marca)


# mostrar apnas os BMW
print("----------------")
for c in lista_carros:
    if c.marca == 'BMW':
        print(c.modelo)


print("----------------")

# pedir ao utilizador um ano e mostrar todos os carros com esse ano

ano = int(input("Digite um ano: "))

contador = 0
for c in lista_carros:
    if c.ano == ano:
        print(c.modelo)
        contador += 1


if contador == 0:
    print("Nenhum carro encontrado")