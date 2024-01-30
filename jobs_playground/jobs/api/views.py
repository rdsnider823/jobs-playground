from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Job, JobTypeChoices
from .serializers import JobSerializer

User = get_user_model()


class JobViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset

    def list(self, request):
        queryset = self.get_queryset()

        params = self.request.query_params

        job_types = [type for type in params.get("job_types", "").split(",") if type]
        if len(job_types) > 0:
            queryset = queryset.filter(job_type__in=job_types)

        if search := params.get("search"):
            queryset = queryset.filter(title=search)

        serializer = JobSerializer(queryset, many=True)
        return Response(serializer.data)
