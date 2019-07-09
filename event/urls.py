from django.urls import path
from . import views

urlpatterns = [
    # ex: /events/
    path('', views.index, name='home'),
    # ex: /events/5
    path('<int:event_id>/', views.event, name='event'),
    path('create-event', views.create_new_event, name='create-event'),
    path('create-event-object', views.create_event_object, name='create-event-object'),
    path('join-event', views.join_event, name='join-event')
]

