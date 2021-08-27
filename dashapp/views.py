from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.


class Dashboard(ListView):
    template_name = 'dashboard/index.html'
    model = Post