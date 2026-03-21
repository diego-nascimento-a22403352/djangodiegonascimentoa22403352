from django.contrib import admin
from .models import Quiz

class QuizAdmin(admin.ModelAdmin):
    list_display = ("titulo", "num_perguntas",)
    ordering = ("titulo", "num_perguntas",)
    search_fields = ("titulo",)

admin.site.register(Quiz, QuizAdmin)