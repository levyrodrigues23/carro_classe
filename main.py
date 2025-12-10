from carro import Carro
from carro_esportivo import CarroSportivo
from carro_inteligente import CarroInteligente
from carro_corrida import CarroCorrida

def test_drive(carro):
    print(f"\n testando carro {carro.__class__.__name__}:")
    carro.acelera()
    carro.exibe_velocidade()

if __name__ == "__main__":
    #testando carro inteligente
    carro_inteligente = CarroInteligente(10)
    carro_inteligente.estaciona()
    test_drive(carro_inteligente)
    
    
    # testando carro esportivo
    
    carro_sportivo = CarroSportivo(50)
    print("carro esportivo: ")
    carro_sportivo.turbo()
    test_drive(carro_sportivo) # aqui que o polimorfismo esta presente
    
    
    # testando carro corrida
    carro_corrida = CarroCorrida(100)
    test_drive(carro_corrida)