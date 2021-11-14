import uuid
from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import mail_admins, send_mail
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.html import mark_safe

from main import forms, models
from srdce import settings


def index(request):
    # calculate today's week
    now = datetime.now().date()
    monday_this_week = now - timedelta(days=now.weekday())

    # calculate next and previous weeks to the one requested
    previous_monday = monday_this_week - timedelta(days=7)
    next_monday = monday_this_week + timedelta(days=7)

    return render(
        request,
        "main/index.html",
        {
            "assignments": models.Assignment.objects.filter(
                week_start=monday_this_week
            ),
            "is_todays": True,
            "current": monday_this_week,
            "current_endweek": monday_this_week + timedelta(days=6),
            "previous": previous_monday,
            "next": next_monday,
        },
    )


def rota(request, isodate):
    # calculate today's week
    now = datetime.now().date()
    monday_this_week = now - timedelta(days=now.weekday())

    # calculate requested week
    date_requested = datetime.strptime(isodate, "%Y-%m-%d").date()
    monday_that_week = date_requested - timedelta(days=date_requested.weekday())

    # if date is not a Monday, redirect to the Monday of that week
    if date_requested.weekday() != 0:
        return redirect("rota", isodate=monday_that_week.date())

    # calculate next and previous weeks to the one requested
    previous_monday = monday_that_week - timedelta(days=7)
    next_monday = monday_that_week + timedelta(days=7)

    return render(
        request,
        "main/index.html",
        {
            "assignments": models.Assignment.objects.filter(
                week_start=monday_that_week
            ),
            "is_todays": monday_this_week == monday_that_week,
            "todays": monday_this_week,
            "current": monday_that_week,
            "current_endweek": monday_that_week + timedelta(days=6),
            "previous": previous_monday,
            "next": next_monday,
        },
    )


def notification(request):
    if request.method == "POST":
        form = forms.NotificationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            if models.Notification.objects.filter(email=email).exists():
                messages.info(request, "This one already exists")
                return redirect("notification")
            form.save()
            messages.success(request, "Notification enabled")
            return redirect("index")
        else:
            messages.error(request, "Invalid input data")
    else:
        form = forms.NotificationForm()

    return render(request, "main/notification.html", {"form": form})


def unsubscribe(request):
    if request.method == "POST":
        form = forms.UnsubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            notifications = models.Notification.objects.filter(email=email)
            if notifications:
                notifications.delete()
                messages.info(request, "Email notification(s) deleted")
                return redirect("unsubscribe")
            else:
                messages.warning(request, "Email does not exist in notifications list")
                return redirect("unsubscribe")
        else:
            messages.error(request, "Invalid email")
    else:
        form = forms.UnsubscribeForm()

    return render(request, "main/unsubscribe.html", {"form": form})


def unsubscribe_oneclick(request, key):
    form = forms.UnsubscribeOneclickForm({"key": key})
    if form.is_valid():
        key = form.cleaned_data.get("key")
        notification = models.Notification.objects.filter(key=key)
        if notification:
            notification.delete()
            messages.success(request, "Unsubscribe successful")
        else:
            messages.error(request, "This email is not subscribed")
    else:
        messages.error(request, "Who are you?")

    return redirect("unsubscribe")


def handbook(request):
    return render(request, "main/handbook.html")


@login_required
def write(request):
    if request.method == "POST":
        if not request.user.is_superuser:
            return HttpResponseForbidden()

        form = forms.WriteForm(request.POST)
        if form.is_valid():
            body_content = mark_safe(form.cleaned_data.get("body"))
            dryrun = form.cleaned_data.get("dryrun")

            # calculate today's week
            now = datetime.now().date()
            monday_this_week = now - timedelta(days=now.weekday())

            # product email content
            this_week_assignments = models.Assignment.objects.filter(
                week_start=monday_this_week
            )
            rota_content = ""
            for a in this_week_assignments:
                rota_content += a.mate.name + " — " + a.job.title + "\n"

            # handle dry run case
            if dryrun:
                mail_admins(
                    "Clean hearts!",
                    render_to_string(
                        "main/rota_announce_custom_email.txt",
                        {
                            "domain": get_current_site(request).domain,
                            "body": body_content,
                            "rota": rota_content,
                            "key": uuid.uuid4(),
                        },
                        request=request,
                    ),
                )
                messages.success(request, "Dry run executed")
                return render(request, "main/write.html", {"form": form})

            # sent notifications
            for n in models.Notification.objects.all():
                if n.is_active:
                    send_mail(
                        "Clean hearts!",
                        render_to_string(
                            "main/rota_announce_custom_email.txt",
                            {
                                "domain": get_current_site(request).domain,
                                "body": body_content,
                                "rota": rota_content,
                                "key": n.key,
                            },
                            request=request,
                        ),
                        settings.DEFAULT_FROM_EMAIL,
                        [n.email],
                    )
                    models.NotificationSent.objects.create(notification=n)

            # finish
            messages.success(request, "Proper run executed")
        else:
            messages.error(request, "Invalid email")
    else:
        form = forms.WriteForm()

    return render(request, "main/write.html", {"form": form})


def issues(_):
    return redirect(
        "https://docs.google.com/spreadsheets/d/1P8AMO3dft0-TzZxGo9tRo-1Ts2-op0SiezZxxbdAjxM/edit?usp=sharing"
    )


def specifications(request):
    return render(request, "main/specifications.html")


def wifi(request):
    return render(request, "main/wifi.html")


def meetups(request):
    return render(request, "main/meetups.html")


def hotwater(request):
    return render(request, "main/hotwater.html")


def party(request):
    return render(request, "main/party.html")


# TODO
def generate_week(request):
    # get jobs
    jobs = models.Job.objects.filter(is_active=True)

    # identify mates with week off

    # get mates
    mates = models.Mate.objects.filter(is_active=True)
    for m in mates:
        # copy active queue of jobs

        # remove jobs mate has done in the past couple of weeks

        # create assignment

        # remove job done from active queue of jobs
        pass
