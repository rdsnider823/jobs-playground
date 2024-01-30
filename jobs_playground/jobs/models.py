from django.db import models

from jobs_playground.core.models import BaseModel


class JobTypeChoices(models.TextChoices):
    FULL_TIME = "full-time", "Full-time"
    PART_TIME = "part-time", "Part-time"
    CONTRACT = "contract", "Contract"
    INTERNSHIP = "internship", "Internship"
    UNSPECIFIED = "unspecified", "Unspecified"


class Job(BaseModel):
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    job_type = models.CharField(max_length=12, choices=JobTypeChoices.choices)
    description = models.TextField(max_length=10000)
    posted_at = models.DateField()
