from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from main import models


class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)


admin.site.register(models.User, UserAdmin)


class MateAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "joined_at")


admin.site.register(models.Mate)


class JobAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "is_active")


admin.site.register(models.Job, JobAdmin)


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("id", "mate", "job", "week_start")


admin.site.register(models.Assignment, AssignmentAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "key", "is_active")


admin.site.register(models.Notification, NotificationAdmin)


class NotificationSentAdmin(admin.ModelAdmin):
    list_display = ("id", "notification", "sent_at")


admin.site.register(models.NotificationSent, NotificationSentAdmin)
