class Carro():
    """Documentação para a classe Carro"""
    
    def __init__(self, brand, model, year, plate, identification, color, side_color, speed, consumption, kind_fuel):
        """Método construtor para a Classe Carro"""
        
        self.marca = brand
        self.modelo = model
        self.ano = year
        self.placa = plate
        self.chassi = identification
        self.cor = color
        self.cor_lateral = side_color
        self.velocidade = speed
        self.consumo = consumption
        self.tipo_compustivel = kind_fuel
    
    def __str__(self):
        """Método para retorno dos dados de um carro"""
    
        retorno = "Carro: {} - {}\n".format(self.marca, self.modelo)
        retorno += "Identificação: {} - {}\n".format(self.placa, self.chassi)
        retorno += "Ano: {} Velocidade: {}\n".format(self.ano, self.velocidade)
        retorno += "Cores {}, {}\n".format(self.cor, self.cor_lateral)
        retorno += "Consumo: {} de {} por km".format(self.consumo, self.tipo_compustivel)
        
        return retorno
        
    def movimentar(self):
        pass
    
    def parar(self):
        pass
    
    def acelerar(self):
        pass
    
    def estacionar(self):
        pass
    
    def get_velocidade(self):
        return self.velocidade