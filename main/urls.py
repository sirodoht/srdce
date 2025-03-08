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
    path("party-xmas-2021/", views.party_xmas_2021, name="party-xmas-2021"),
    path("party-may-2022/", views.party_may_2022, name="party_may_2022"),
    path("party-oct-2022/", views.party_oct_2022, name="party_oct_2022"),
    path("party-xmas-2022/", views.party_xmas_2022, name="party-xmas-2022"),
    path("party-oct-2023/", views.party_oct_2023, name="party-oct-2023"),
    path("party-feb-2023/", views.party_feb_2023, name="party-feb-2023"),
    path("party-apr-2025/", views.party_apr_2025, name="party-apr-2025"),
    path("party/", views.party_apr_2025, name="party-apr-2025"),
    path("manuals/", views.manuals, name="manuals"),
]
