from django.db import models

# Create your models here.

class Chassi(models.Model):
    numero = models.CharField ('Chassi', max_length=16, help_text='Informe 16 caracteres')

    class Meta:
        verbose_name='Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero

class Carro(models.Model):
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    modelo = models.CharField ('Modelo', max_length=30, help_text='Maximo 30 caracteres')
    preco = models.DecimalField ('Preço', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name='Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return self.modelo