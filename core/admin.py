from django.contrib import admin

# Register your models here.
from core.models import Chassi, Carro, Montadora

@admin.register (Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display=('nome',)

@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero', )

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('montadora', 'modelo', 'chassi', 'preco')

    def get_motoristas(self, obj):
        return ', '.join([m.username for m in obj.motoristas.all()])