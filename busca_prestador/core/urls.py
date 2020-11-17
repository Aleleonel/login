from django.urls import path
from . import views as v

app_name = 'core'

urlpatterns = [
    path('', v.login, name='login'),
    path('home/', v.home, name='home'),
]
