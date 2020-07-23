from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>",views.entry, name="entry"),
    path("wiki/edit/<str:entry>",views.edit,name="edit"),
 ]
