from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Devices
from .forms import DeviceForm


def index(request):
    return render(request, 'prob/index.html')


def input(request, id):
    context = {
        'id': id
    }
    return render(request, 'prob/input.html', context)


class DevicesFormView(CreateView):
    template_name = 'prob/form.html'
    form_class = DeviceForm
    success_url = reverse_lazy('devices')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['devices'] = Devices.objects.all()
    #     return context


class DevicesListView(ListView):
    model = Devices
