from django.contrib import admin
from cursos.models import Assunto, Modulo, Curso


@admin.register(Assunto)
class AssuntoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'slug']
    prepopulated_fields = {'slug': ('titulo',)}


class ModuloInline(admin.StackedInline):
    model = Modulo


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'assunto', 'criado']
    list_filter = ['assunto', 'criado']
    search_fields = ['titulo', 'desc_geral']
    prepopulated_fields = {'slug': ('titulo',)}
    inlines = [ModuloInline]
