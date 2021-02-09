from django.contrib import admin

from main import models


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
