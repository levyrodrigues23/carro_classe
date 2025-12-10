from carro import Carro

class CarroInteligente(Carro):
    def __init__(self, velocidade_inicial):
        super().__init__(velocidade_inicial)
        
    def estaciona(self):
        print("estacionando automaticamente...")