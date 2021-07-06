from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('application_form', views.application_form, name="application-form"),
    path('programs', views.programs, name="programs"),
]