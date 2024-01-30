from django.db import migrations

from django.contrib.auth.hashers import make_password
from django.db import migrations
import csv


def create_jobs(apps, schema_editor):
    Job = apps.get_model("jobs", "Job")
    with open("jobs_playground/jobs/migrations/data/jobs.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Job.objects.create(**row)


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_jobs),
    ]