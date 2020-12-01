from django.contrib import admin


from .models import Instalacao


class InstalacaoAdmin(admin.ModelAdmin):
    list_display = (
        'placa',
        'nome',
        'endereco',
        'tel01',
        'tel02',
        'vendedor',
        'instalador',
        'data_pedido',
        'instalado',
        'vistoria',
        'obs',
    )


admin.site.register(Instalacao, InstalacaoAdmin)

