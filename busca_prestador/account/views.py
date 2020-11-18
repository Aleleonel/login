# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('/login/')
    template_name = 'account/register.html'


def registrar(request):
    # Se dados forem passados via POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():  # se o formulario for valido
            form.save()  # cria um novo usuario a partir dos dados enviados
            return redirect("/login/")  # redireciona para a tela de login
        else:
            # mostra novamente o formulario de cadastro com os erros do formulario atual
            return render(request, "account/register.html", {"form": form})

    # se nenhuma informacao for passada, exibe a pagina de cadastro com o formulario
    return render(request, "account/register.html", {"form": UserCreationForm()})