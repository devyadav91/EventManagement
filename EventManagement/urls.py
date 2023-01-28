from event import views
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register('events',views.eventapiview,basename='events') 
route.register('calender',views.calenderapiview,basename='calender')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(route.urls)),
]
