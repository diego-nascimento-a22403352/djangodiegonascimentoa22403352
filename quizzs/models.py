from django.db import models

# Create your models here.
class Quiz(models.Model):
    titulo = models.CharField(max_length=100)
    num_perguntas = models.IntegerField()

    def __str__(self):
        return f'{self.titulo}: {self.num_perguntas} perguntas'