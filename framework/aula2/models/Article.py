from django.db import models
from .Reporter import Reporter

class Article(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    public_data = models.DateField(verbose_name='Data de Publicação')
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}: {} - {}".format(self.reporter, self.titulo, self.public_data)