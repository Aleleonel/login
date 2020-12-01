from django.contrib import admin

from image.models import Imagens


class ImagensAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'fotos',
    )


admin.site.register(Imagens, ImagensAdmin)