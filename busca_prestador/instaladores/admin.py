from django.contrib import admin

from .models import Instaladores


class InstaladoresAdmin(admin.ModelAdmin):
    pass


admin.site.register(Instaladores, InstaladoresAdmin)
