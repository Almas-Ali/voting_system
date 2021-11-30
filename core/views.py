from django.shortcuts import render
import config


context = {'config': config}


def index(request):
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html', context)


def vote(request):
    return render(request, 'vote.html', context)


def result(request):
    return render(request, 'result.html', context)
