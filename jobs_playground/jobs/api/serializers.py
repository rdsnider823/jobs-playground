from django.contrib.auth import get_user_model
from rest_framework import serializers

from jobs_playground.jobs.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["id", "company", "title", "job_type", "posted_at"]
