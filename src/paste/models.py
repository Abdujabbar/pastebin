from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
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
    content = models.CharField(max_length=50000)
    expired_at = models.DateTimeField(default=get_next_30th_day)
    short_url = models.CharField(max_length=8)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.pk}: {self.short_url}" 

    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)
