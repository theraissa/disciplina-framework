from django.db import models

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    ano =   models.IntegerField()
    chassi = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    placa = models.CharField(max_length=7)
    
    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.modelo, self.ano, self.chassi, self.cor, self.placa)