from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.views import generic
# from django.utils import timezone
# from rps.game_rps import *

# Create your views here.


def home_index(request):
    return render(request, 'home/index.html')
