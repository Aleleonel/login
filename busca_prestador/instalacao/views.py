from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView
from .forms import InstalacaoForm
from .models import Instalacao


def lista_search(request):
    template_name = 'instalacao/instalacao_lista.html'
    search = request.GET.get('search')
    search2 = request.GET.get('search2')

    if search:

        objects_list = Instalacao.objects.filter(placa__icontains=search)
        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)

    if search2:
        objects_list = Instalacao.objects.filter(instalado__icontains=search2)
        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)

    else:
        objects_list = Instalacao.objects.all()
        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)


def instalacao_detail(request, pk):
    template_name = 'instalacao/instalacao_detail.html'
    obj = Instalacao.objects.get(pk=pk)

    context = {
        'object': obj
    }
    return render(request, template_name, context)


def endereco_add(request):
    template_name = 'instalacao/instalacao_form.html'
    return render(request, template_name)


def instalacao_delete(request, pk):
    instalacao = get_object_or_404(Instalacao, pk=pk)
    instalacao.delete()
    return HttpResponseRedirect('/')


class InstalacaoCreate(CreateView):
    model = Instalacao
    template_name = 'instalacao/instalacao_form.html'
    form_class = InstalacaoForm


class InstalacaoUpdate(UpdateView):
    model = Instalacao
    template_name = 'instalacao/instalacao_form.html'
    form_class = InstalacaoForm

