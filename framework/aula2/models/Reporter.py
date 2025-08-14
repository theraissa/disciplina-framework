from django.db import models

class Reporter(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome Completo')
    email = models.EmailField(verbose_name='E-mail')
    cpf = models.CharField(max_length=11, verbose_name='Número do CPF')

    def __str__(self):
        return "{} - {} - {}".format(self.nome, self.email, self.cpf)