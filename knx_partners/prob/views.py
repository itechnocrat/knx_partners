from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from .forms import NameForm


# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/prob/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'prob/name.html', {'form': form})


def index(request):
    return render(request, 'prob/index.html')


def input(request, id):
    context = {
        'id': id
    }
    return render(request, 'prob/input.html', context)


def output(request, id):
    context = {
        'id': id
    }
    return render(request, 'prob/output.html', context)


def device(request, id):
    context = {
        'id': id
    }
    return render(request, 'prob/device.html', context)


def sensor(request, id):
    context = {
        'id': id
    }
    return render(request, 'prob/sensor.html', context)


def devicewa(request, id):
    context = {
        'id': id
    }
    return render(request, 'prob/devicewa.html', context)


def socket(request, id):
    context = {
        'id': id
    }
    return render(request, 'prob/socket.html', context)


def light(request, id):
    context = {
        'id': id
    }
    return render(request, 'prob/light.html', context)
