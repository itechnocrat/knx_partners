from .models import Device
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import DeviceForm


def index(request):
    return render(request, 'prob/index.html')


def input(request, id):
    context = {
        'id': id
    }
    return render(request, 'prob/input.html', context)


class DeviceFormView(CreateView):
    template_name = 'prob/form.html'
    form_class = DeviceForm
    success_url = reverse_lazy('form')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['devices'] = Device.objects.all()
        return context
