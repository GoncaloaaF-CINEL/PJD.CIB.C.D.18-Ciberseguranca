from dataclasses import dataclass


@dataclass
class Carro:
    marca: str
    modelo: str
    ano: int
    andar: bool = False
    velocidade: int = 0

    def arrancar(self):
       if self.andar:
                print("Carro já está amdar")
         else:
                print("Carro arrancou")
                self.andar = True
                self.velocidade = 1


    def acelerar(self, velo):
        if self.andar:
            self.velocidade += velo
            print(f"Carro acelerou {velo} km/h")
        else:
            print("Carro não está andando")

    
    def travar_para(self, velo):
        if self.andar:

            if velo > self.velocidade:
                print("Carro não pode diminuir mais que a velocidade atual")
                return

            self.velocidade = velo
            print(f"Carro diminu para {velo} km/h")



        else:
            print("Carro não está andando")


    def parar(self):
        if self.andar:
            self.andar = False
            print("Carro parou")

        else:
            print("Carro já está parado")



