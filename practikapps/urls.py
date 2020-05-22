from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('practikapps/', include('practikapps.urls')),
]

urlpatterns = [
    path('', views.index, name='index'),
]