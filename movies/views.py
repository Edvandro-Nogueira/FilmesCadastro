from django.shortcuts import render
#from rest_framework import viewsets
#from movies.models import Movies
#from movies.api.serializers import MoviesSerializer

# Create your views here.
#class MoviesViewSet(viewsets.ModelViewSet):
#    queryset = Movies.objects.all()
#    serializer_class = MoviesSerializer
import movies
from movies import models


def index(request):
    lista = models.Movies.objects.all()
    context = {
        'lista': lista,
    }
    return render(request, "index.html", context)