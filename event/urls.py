from django.urls import path
from . import views

urlpatterns = [
    # ex: /events/
    path('', views.index, name='home')

]

