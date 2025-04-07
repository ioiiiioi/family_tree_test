from django.db import models
from django.contrib.auth.models import User

class BaseModels(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class CreatorModels(BaseModels):
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        abstract=True