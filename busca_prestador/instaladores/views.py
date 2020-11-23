from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView
from .forms import InstaladoresForm
from .models import Instaladores


def lista_search(request):
    template_name = 'instaladores/instaladores_lista.html'
    search = request.GET.get('search')

    if search:

        objects_list = Instaladores.objects.filter(nome__icontains=search)
        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)
    else:
        objects_list = Instaladores.objects.all()
        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)


def instaladores_detail(request, pk):
    template_name = 'instaladores/instaladores_detail.html'
    obj = Instaladores.objects.get(pk=pk)

    context = {
        'object': obj
    }
    return render(request, template_name, context)


def instaladores_add(request):
    template_name = 'instaladores/instaladores_form.html'
    return render(request, template_name)


def instaladores_delete(request, pk):
    instaladores = get_object_or_404(Instaladores, pk=pk)
    instaladores.delete()
    return HttpResponseRedirect('/')


class InstaladoresCreate(CreateView):
    model = Instaladores
    template_name = 'instaladores/instaladores_form.html'
    form_class = InstaladoresForm


class InstaladoresUpdate(UpdateView):
    model = Instaladores
    template_name = 'instaladores/instaladores_form.html'
    form_class = InstaladoresForm
