from django.db import models
from .Pessoa import Pessoa

class Passaporte(models.Model):
    numero = models.CharField(max_length=100, verbose_name='Número')
    data_criacao = models.DateField(verbose_name='Data Criação')
    data_exp = models.DateField(verbose_name='Data Expiração')
    dono = models.OneToOneField(Pessoa, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return "{}:{}:{} - {}".format(self.numero, self.data_criacao, self.data_exp, self.dono)