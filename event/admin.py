from django.contrib import admin
from .models import events,calender

@admin.register(events)
class eventAdmin(admin.ModelAdmin):
    list_display =['message','event_start','event_end']

@admin.register(calender)
class eventAdmin(admin.ModelAdmin):
    list_display =['id','user']