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
    path("specs/", views.specifications, name="specifications"),
    path("wifi/", views.wifi, name="wifi"),
    path("meetups/", views.meetups, name="meetups"),
    path("hotwater/", views.hotwater, name="hotwater"),
    path("manuals/", views.manuals, name="manuals"),
    path("party-xmas-2021/", views.xmas_party_2021, name="party-xmas-2021"),
    # path("party/", views.party, name="party"),
]
