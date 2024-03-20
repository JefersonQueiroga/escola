from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()

    def __str__(self):
        return self.nome + " " + str(self.carga_horaria)

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    sigla_estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class AreaInteresse(models.Model):
    nome = models.CharField(max_length=100)
   
    def __str__(self):
        return self.nome
    
# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    data_nascimento = models.DateField()
    matricula = models.CharField(max_length=12)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)
    area_interesse = models.ManyToManyField(AreaInteresse)
    
    def __str__(self):
        return self.email



