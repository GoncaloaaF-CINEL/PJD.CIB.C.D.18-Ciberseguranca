import sys


"""
tipos de dados
var
op
in/out

condições
loops

listas e tuplas


Funções

"""


"""

int - 1 ,23123, 3124234324
float - 1.0, 1.1, 1.2
str - "aeqwwqe", "eqwewqeb", "ewqewqec"

"""

lista_pessoas = []

while True:
    nome = input("nome: ").strip()
    idade = int(input("idade: "))
    adulto = False
    print(f"olá {nome.capitalize()}", end=",")
    print(f"tens {idade}")


    if idade >= 18:
        print("Ja es Adulto !!")
        adulto = True
    else:
        aux = 18 - idade
        print(f"esta quase so falta {aux} anos !!")
        adulto = False


    pessoa = (nome, idade, adulto)
    lista_pessoas.append(pessoa)

    next = input("proximo? (s/n): ")

    if next == "n":
        break

"""
print(lista_pessoas)

p = lista_pessoas[0]
print(p)

n = p[0]
print(n)

l = n[0]
print(l)

p = lista_pessoas[0]
n = lista_pessoas[0][0]
l = lista_pessoas[0][1][4]
print(l)
"""

for p in lista_pessoas:
    print("-------------------")
    print(f"nome: {p[0]}")
    print(f"idade: {p[1]}")
    if p[2]:
        print("Adulto")
    else:
        print("Menor")

    print("-------------------")