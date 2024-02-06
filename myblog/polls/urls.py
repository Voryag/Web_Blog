from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_home, name="index_home"),
    path("redirect_create_page/", views.redirect_create_page, name="redirect_create_page"),
    path("create_notification_page/", views.new_create_page, name="create_notification_page.html")
]