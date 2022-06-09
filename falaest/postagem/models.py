from django.db import models



class Postagem(models.Model):
    nome_estagiario = models.CharField(max_length=30)
    postagem = models.TextField(max_length=200)


