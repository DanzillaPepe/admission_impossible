from django.urls import path

from . import views

app_name = 'adm_lists'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('directions', views.DirectionsView, name='directions')

]