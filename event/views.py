from django.shortcuts import render
from .models import Event, JoinEvent


# Create your views here.
def index(request):
    latest_event_list = Event.objects.order_by('-pub_date')[:10]
    context = {'latest_event_list': latest_event_list}
    return render(request, 'events/index.html', context)