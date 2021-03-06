from datetime import datetime, timedelta

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from main import models


class Command(BaseCommand):
    help = "Populate database with development data."

    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise CommandError("Population canceled. Django settings NODEBUG is on.")

        self.stdout.write(self.style.NOTICE("Initiating development data population."))

        # create mates
        mate_a = models.Mate.objects.create(name="Sophie")
        mate_b = models.Mate.objects.create(name="Peter")
        mate_c = models.Mate.objects.create(name="Susan")
        mate_d = models.Mate.objects.create(name="Otis")
        mate_e = models.Mate.objects.create(name="Ezra")
        mate_f = models.Mate.objects.create(name="Mark")

        # create jobs
        job_a = models.Job.objects.create(title="Kitchen")
        job_b = models.Job.objects.create(title="Living Room")
        job_c = models.Job.objects.create(title="Toilet")
        job_d = models.Job.objects.create(title="Stairs")
        job_e = models.Job.objects.create(title="Windows")
        job_f = models.Job.objects.create(title="Bins")

        # create assignments
        now = datetime.now().date()
        monday_this_week = now - timedelta(days=now.weekday())
        models.Assignment.objects.create(
            mate=mate_a, job=job_a, week_start=monday_this_week
        )
        models.Assignment.objects.create(
            mate=mate_b, job=job_b, week_start=monday_this_week
        )
        models.Assignment.objects.create(
            mate=mate_c, job=job_c, week_start=monday_this_week
        )
        models.Assignment.objects.create(
            mate=mate_d, job=job_d, week_start=monday_this_week
        )
        models.Assignment.objects.create(
            mate=mate_e, job=job_e, week_start=monday_this_week
        )
        models.Assignment.objects.create(
            mate=mate_f, job=job_f, week_start=monday_this_week
        )
