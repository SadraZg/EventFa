from django.shortcuts import render, redirect
from .models import Event, JoinEvent
from django.http import Http404
from django.contrib.auth.views import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

pass_salt = '@131@13551eded'


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


@login_required
def logout_user(request):
    logout(request)
    return redirect('/')


def validate_user(request):
    result = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=make_password(password, pass_salt))

        print(user)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/account/dashboard')
            else:
                result = 'user is suspended!'
        else:
            print("Someone tried to login and failed.")
            print("They used Mail: {} and Password: {}".format(username, password))
            result = 'username or password is wrong'
    else:
        result = 'please use POST method'

    return render(request, 'registration/login.html', {'result': result})


def register(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        cellphone = request.POST.get('cellphone')

        if mail and first_name and last_name and cellphone and username is None:
            return None

        user = User.objects.create_user(username, email=mail,
                                        password=make_password(password, pass_salt),
                                        first_name=first_name, last_name=last_name)
        # user.date_joined = datetime.now()

        user.save()
        if user is not None:
            login(request, user)
            return redirect('/account/dashboard')
        else:
            result = 'user already exists'

            # send an activation mail to user
        return render(request, 'registration/login.html', {'result': result})


