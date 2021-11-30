from django.shortcuts import render
import config


context = {'config': config}


def index(request):
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html', context)
