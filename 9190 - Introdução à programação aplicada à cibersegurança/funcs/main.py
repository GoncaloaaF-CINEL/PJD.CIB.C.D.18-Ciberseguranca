
def nome():
    print("Ola Mundo")


nome()
nome()
nome()
nome()

print("-------------------")

def olaMundo(my_name):
    print(f"Ola Mundo, {my_name.capitalize()}")


olaMundo("Lucas")
olaMundo("joao")
olaMundo("MaRiA")
olaMundo("aNA")

print("-------------------")


def olaMundo2(my_name: str):
    print(f"Ola Mundo, {my_name.capitalize()}")



print("-------------------")



def saudacao(nome: str, idade: int):
    print(f"{idade}, {nome.capitalize()}")


saudacao("Lucas", 25)
saudacao("Lucas", idade=25)
saudacao(idade=25, nome="Lucas")


print("----------saudacao_2---------")

def saudacao_2(nome: str, idade: int) -> str:
   return f"{idade}, {nome.capitalize()}"



msg = saudacao_2("Lucas", 25)
print(msg)




print("-------------------")



