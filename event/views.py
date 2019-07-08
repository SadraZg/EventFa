from django.shortcuts import render, redirect
from .models import Event, JoinEvent
from django.http import Http404
from django.contrib.auth.views import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    latest_event_list = Event.objects.order_by('-pub_date')[:10]
    context = {'latest_event_list': latest_event_list}
    return render(request, 'events/index.html', context)


def event(request, event_id):
    try:
        specific_event = Event.objects.get(pk=event_id)
        user_status = None
        # If user is authenticated then check the status of it's last request
        if request.user.is_authenticated:
            for i in JoinEvent.objects.filter(event=specific_event, user=request.user):
                user_status = i
    except Event.DoesNotExist:
        raise Http404("رویداد موردنظر وجود ندارد!")
    return render(request, 'events/detail.html', {'event': specific_event, 'user_status': user_status})
