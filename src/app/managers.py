from django.db import models
from django.utils import timezone


class PasteActiveRecordsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(expired_at__gt=timezone.now())
