from django.urls import path

from . import views

urlpatterns = [
    #path("", views.render_home, name="render_home"),
    path("", views.render_home, name="render_home"),
]