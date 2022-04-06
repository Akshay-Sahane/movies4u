from django.urls import path
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('',TemplateView.as_view(template_name="movie/index.html"),name="Home"),

    path('add-bmovie/',BmovieCreateView.as_view(),name="addbollymovie"),
    path('add-hmovie/',HmovieCreateView.as_view(),name="addhollymovie"),

    path('Bmovielist/',BmovieListView.as_view(),name="Bmovielist"),
    path('Hmovielist/',HmovieListView.as_view(),name="Hmovielist"),

    path('update-bmovie/<int:pk>',BmovieUpdateView.as_view(),name="update-bmovie"),
    path('update-hmovie/<int:pk>',HmovieUpdateView.as_view(),name="update-hmovie"),

    path('delete-bmovie/<int:pk>',BmovieDeleteView.as_view(),name='delete-bmovie'),
    path('delete-hmovie/<int:pk>',HmovieDeleteView.as_view(),name='delete-hmovie'),

    path('searchmovie',searchmovie),

    path('moviesortnameascB',moviesortnameascB),
    path('moviesortnamedescB',moviesortnamedescB),

    path('moviesortdateascB',moviesortdateascB),
    path('moviesortdatedescB',moviesortdatedescB),

    path('moviesortnameascH',moviesortnameascH),
    path('moviesortnamedescH',moviesortnamedescH),

    path('moviesortdateascH',moviesortdateascH),
    path('moviesortdatedescH',moviesortdatedescH),
    path('about',about,name="about")
]