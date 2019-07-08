from django.urls import path
from . import views

urlpatterns = [
    # ex: /events/
    path('', views.index, name='home'),
    # ex: /events/5
    path('<int:event_id>/', views.event, name='event')

]

