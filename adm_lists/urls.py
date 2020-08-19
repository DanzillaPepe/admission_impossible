from django.urls import path

from . import views

app_name = 'adm_lists'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

]