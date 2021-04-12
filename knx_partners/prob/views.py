from django.shortcuts import render


def index(request):
    return render(request, 'prob/index.html')


def input(request, id):
    context = {
        'id': id
    }
    return render(request, 'prob/input.html', context)
