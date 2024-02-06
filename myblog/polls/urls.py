from django.urls import path
from . import views

urlpatterns = [
    path("", views.render_index, name="render_index"),
    path("create/", views.redirect_create_page, name="create"),
    path("delete/", views.redirect_create_page, name="delete"),
]