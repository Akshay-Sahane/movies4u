import re
from django.shortcuts import redirect, render

from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import BMovie,HMovie
from .forms import BForm,HForm
from django.urls import reverse_lazy

# CreateView is used for creation,updation,deletion
class BmovieCreateView(SuccessMessageMixin,CreateView):
    model = BMovie
    form_class=BForm
    template_name = "movie/movieform.html"
    success_message="bollywood movie is added successfully..."
    success_url=reverse_lazy('Bmovielist')


class HmovieCreateView(SuccessMessageMixin,CreateView):
    model = HMovie
    form_class=HForm
    template_name = "movie/hmovieform.html"
    success_message="hollywood movie is added successfully..."
    success_url=reverse_lazy('Hmovielist')

from django.views.generic.list import ListView

class BmovieListView(ListView):
    model = BMovie
    template_name = "movie/Bmovielist.html"

class HmovieListView(ListView):
    model = HMovie
    template_name = "movie/Hmovielist.html"

from django.views.generic.edit import UpdateView

class BmovieUpdateView(SuccessMessageMixin,UpdateView):
    model = BMovie
    form_class=BForm
    template_name ="movie/movieform.html"
    success_message="movie Is Updated Successfully..."
    success_url=reverse_lazy("Bmovielist")

class HmovieUpdateView(SuccessMessageMixin,UpdateView):
    model = HMovie
    form_class=HForm
    template_name ="movie/movieform.html"
    success_message="movie Is Updated Successfully..."
    success_url=reverse_lazy("Hmovielist")

from django.views.generic.edit import DeleteView

class BmovieDeleteView(SuccessMessageMixin,DeleteView):
    model = BMovie
    template_name = "movie/delete_confirm.html"
    success_message="movie is Deleted Successfully..."
    success_url = reverse_lazy("Bmovielist")

class HmovieDeleteView(SuccessMessageMixin,DeleteView):
    model = HMovie
    template_name = "movie/delete_confirm.html"
    success_message="movie is Deleted Successfully..."
    success_url = reverse_lazy("Hmovielist")


def moviesortnameascB(req):
    mlist=BMovie.objects.order_by('-movieName')
    context={'object_list':mlist}
    return render(req,"movie/Bmovielist.html",context)

def moviesortnamedescB(req):
    mlist=BMovie.objects.order_by('movieName')
    context={'object_list':mlist}
    return render(req,"movie/Bmovielist.html",context)

def moviesortdateascB(req):
    mlist=BMovie.objects.all().order_by('movieReleasedate')
    context={'object_list':mlist}
    return render(req,"movie/Bmovielist.html",context)

def moviesortdatedescB(req):
    mlist=BMovie.objects.all().order_by('-movieReleasedate')
    context={'object_list':mlist}
    return render(req,"movie/Bmovielist.html",context)

def moviesortnameascH(req):
    mlist=HMovie.objects.order_by('movieName')
    context={'object_list':mlist}
    return render(req,"movie/Hmovielist.html",context)

def moviesortnamedescH(req):
    mlist=HMovie.objects.order_by('-movieName')
    context={'object_list':mlist}
    return render(req,"movie/Hmovielist.html",context)

def moviesortdateascH(req):
    mlist=HMovie.objects.order_by('-movieReleasedate')
    context={'object_list':mlist}
    return render(req,"movie/Hmovielist.html",context)

def moviesortdatedescH(req):
    mlist=HMovie.objects.order_by('movieReleasedate')
    context={'object_list':mlist}
    return render(req,"movie/Hmovielist.html",context)

from django.contrib import messages
def searchmovie(req):
    q=req.GET['q']
    if q:
        l=q.lower()
        blist=BMovie.objects.filter(movieName__contains=l)
        hlist=HMovie.objects.filter(movieName__contains=l)
        if blist:
            context={'object_list':blist}
            return render(req,"movie/Bmovielist.html",context)
        elif hlist:
            context={'object_list':hlist}
            return render(req,"movie/Bmovielist.html",context)
        else:
            messages.warning(req,"No movie found")
            return redirect('Home')
    else:
        messages.warning(req,"please enter movie name to search")
        return redirect('Home')

def about(req):
    return render(req,'movie/about.html')