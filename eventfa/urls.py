
from django.contrib import admin
from django.urls import path
from django.urls import include
from event import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('event.urls')),
    path('registration/', include('django.contrib.auth.urls')),
    path('login-user', views.validate_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register-user', views.register, name='sign-up'),
    path('', views.home, name='home'),
    path('account/dashboard', views.dashboard, name='dashboard'),
    path('account/history', views.history, name='history'),
    path('account/support', views.support, name='support')
]
