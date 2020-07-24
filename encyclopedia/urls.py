from django.urls import path

from . import views
from . import util

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>",views.entry, name="entry"),
    path("wiki/edit/<str:entry>",views.edit,name="edit"),
    path("wiki",views.randomentry,name="randomentry"),
    path("wiki/create/newpage",views.newentry,name="newentry")
 ]
