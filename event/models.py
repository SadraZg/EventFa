from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Event model
class Event(models.Model):
    title = models.CharField(max_length=250, default='رویداد')
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/')
    capacity = models.IntegerField(default=10)
    reserved_number = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    start_time = models.DateTimeField('Start time', default=timezone.now())
    finish_time = models.DateTimeField('Finish time', default=timezone.now())
    address = models.TextField(default='آدرس')
    phone = models.CharField(max_length=12, null=True)
    mail = models.EmailField(null=True)
    instagram = models.CharField(max_length=30, null=True)
    telegram = models.CharField(max_length=30, null=True)
    creator = models.CharField(max_length=250, default='سازنده')

    def remaining(self):
        return self.capacity - self.reserved_number

    def is_full(self):
        if self.capacity == self.reserved_number:
            return True
        else:
            return False

    def __str__(self):
        return self.title


# Model that handle user request
class JoinEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    join_date = timezone.now()
    status = models.BooleanField('status', default=False)
    pending = models.BooleanField('pending', default=True)
