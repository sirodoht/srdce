from django.contrib import admin
from django.urls import path, re_path

from main import views

admin.site.site_header = "srdce administration"

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r"^rota/(?P<isodate>\d{4}-\d{2}-\d{2})/$", views.rota, name="rota"),
    path("notification/", views.notification, name="notification"),
    path("unsubscribe/", views.unsubscribe, name="unsubscribe"),
    path(
        "unsubscribe/<uuid:key>",
        views.unsubscribe_oneclick,
        name="unsubscribe_oneclick",
    ),
    path("write/", views.write, name="write"),
    path("issues/", views.issues, name="issues"),
]
