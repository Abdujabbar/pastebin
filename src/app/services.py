import base64
import hashlib
from django.utils import timezone
from .models import Paste
from django.utils.timezone import make_aware
from datetime import datetime


def generate_random_hash(content, hash_length=8):
    hex_number = hashlib.sha256(content.encode()).hexdigest()
    return base64.b64encode(hex_number.encode()).decode()[:hash_length]


class SharePasteService:
    def execute(self, *args, **kwargs):
        generated_short_url = self.generate_shorten_url(
            kwargs.get("content"), kwargs.get("user").pk
        )
        expired_at = kwargs.get("expired_at")
        if isinstance(expired_at, str):
            expired_at = make_aware(
                datetime.strptime(expired_at, "%Y-%m-%d %H:%M:%S"))

        paste = Paste(
            expired_at=expired_at,
            content=kwargs.get("content"),
            user=kwargs.get("user"),
            short_url=generated_short_url,
            permanent_delete=kwargs.get("permanent_delete"),
            name=kwargs.get("name"),
        )
        paste.clean_fields()
        paste.save()

        return paste

    def generate_shorten_url(self, content, user_id):
        unique_content = f"{content}:{user_id}" f":{timezone.now().microsecond}"
        return generate_random_hash(unique_content)


class MakePasteExpiredService:
    def execute(self, paste, user):
        if paste.user != user:
            paste.expired_at = timezone.now()
            paste.save()
