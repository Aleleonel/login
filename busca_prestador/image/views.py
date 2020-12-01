from django.shortcuts import render, get_object_or_404

from .forms import ImageForm
from .models import Imagens
from instalacao.models import Instalacao


def lista_search(request):
    template_name = 'image/imagens_lista.html'

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                obj = form.instance
                context = {
                    'obj': obj,
                }
                return render(request, template_name, context)

            except:
                pass

    else:
        form = ImageForm()
    img = Imagens.objects.all()
    context = {
        'form': form,
        'img': img
    }
    return render(request, template_name, context)


def imagens_detail(request, pk):
    template_name = 'image/imagens_detail.html'
    instalacao = get_object_or_404(Instalacao, pk=pk)
    imagens = Imagens.objects.filter(instalacao=instalacao)

    context = {
        'imagens': imagens
    }
    return render(request, template_name, context)


