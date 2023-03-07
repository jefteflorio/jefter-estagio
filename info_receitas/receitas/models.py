from django.db import models

class Receitas(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.CharField(max_length=1000)
    def __str__(self):
        return self.nome_receita

