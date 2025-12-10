from carro import Carro

class CarroCorrida(Carro):
    def __init__(self, velocidade_inicial):
        super().__init__(velocidade_inicial)
        
        
    def acelera(self):
        self.velocidade += 5
        print("aceleração de corrida: a velocidade aumentou em 5 km/h")