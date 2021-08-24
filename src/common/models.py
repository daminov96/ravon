from django.db import models
import uuid


class BaseModel(models.Model):
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_created=True)
    updated_At = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

