from django.contrib import admin
from .models import Escola

class EscolaAdmin(admin.ModelAdmin):
    list_display = ("nome", "num_alunos",)
    ordering = ("nome", "num_alunos",)
    search_fields = ("nome",)

admin.site.register(Escola, EscolaAdmin)