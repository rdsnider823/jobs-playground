from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    # The id field is marked as null but we are managing the migrations in a way
    # the not null constraint and idenity is preserved to maintain auto increment.
    # This field is primarily here to support rolling back the code if necessary.
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
