from multiprocessing.synchronize import Event
from django.contrib import admin
from myapp.models import Event

# Register your models here.

admin.site.register(Event)