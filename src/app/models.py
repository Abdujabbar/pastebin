from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .managers import PasteActiveRecordsManager


class TrashableMixin(models.Model):
    deleted_at = models.DateTimeField(default=None, null=True, editable=False)

    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.save()

    @property
    def is_deleted(self):
        if not self.deleted_at:
            return False

        return self.deleted_at < timezone.now()


def get_next_30th_day():
    return timezone.now() + timedelta(30)


class Paste(TrashableMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=50000)
    expired_at = models.DateTimeField(default=get_next_30th_day, null=True)
    short_url = models.CharField(max_length=8, null=True)
    permanent_delete = models.BooleanField(default=False)
    name = models.CharField(max_length=255)

    active_records = PasteActiveRecordsManager()

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.pk}: {self.short_url}"

    def clean_fields(self, *args, **kwargs) -> None:
        if self.expired_at < timezone.now():
            raise ValidationError(
                {"expired_at": "Expired at should be greater than now"}
            )
        return super().clean_fields(*args, **kwargs)
