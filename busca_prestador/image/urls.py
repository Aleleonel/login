from django.urls import path
from . import views as v

app_name = 'image'

urlpatterns = [
    path('', v.lista_search, name='imagens_lista'),
    path('<int:pk>/', v.imagens_detail, name='imagens_detail'),

]