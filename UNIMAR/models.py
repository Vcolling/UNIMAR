from django.db import models

# Create your models here.

class Pessoa(models.Model):
    Nome = models.CharField(max_length=100)
    Telefone = models.CharField(max_length=13)
    Email = models.EmailField()
    Foto = models.ImageField(upload_to='Media')
    Ativo = models.BooleanField(default=True)
    Registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.Nome)

class Empresa(models.Model):
    Nome = models.CharField(max_length=100)
    Telefone = models.CharField(max_length=13)
    Email = models.EmailField()
    Foto = models.ImageField(upload_to='Media/Empresa')
    Ativo = models.BooleanField(default=True)
    Registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.Nome)
