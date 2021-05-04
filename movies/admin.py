from django.contrib import admin
#from movie.models import Movies
from movies.models import Movies


# Register your models here.
class Movie(admin.ModelAdmin):
    list_display = ('Titulo', 'ano', 'diretor', 'genero', 'avaliacao')
    list_display_links = ('Titulo', 'diretor')
    search_fields = ('Titulo', 'ano', 'diretor', 'genero', 'avaliacao',)


admin.site.register(Movies, Movie)
