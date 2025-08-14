from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    data_nasc = models.DateField(verbose_name='Nascimento')
    cpf = models.CharField(max_length=11, verbose_name='Número do CPF')
    
    def __str__(self):
        return "{}:{} - {}".format(self.nome, self.data_nasc, self.cpf)