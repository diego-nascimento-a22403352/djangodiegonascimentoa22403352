from django.contrib import admin
from .models import Ginasio

class GinasioAdmin(admin.ModelAdmin):
    list_display = ("nome", "mensalidade",)
    ordering = ("nome", "mensalidade",)
    search_fields = ("nome",)

admin.site.register(Ginasio, GinasioAdmin)