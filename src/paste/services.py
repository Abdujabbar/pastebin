import base64
from datetime import timezone
import hashlib
from random import randint
from django.utils import timezone
from .models import Paste
import base64


def generate_random_hash(content):
    hex_number = hashlib.sha256(content.encode()).hexdigest()
    return base64.b64encode(hex_number.encode()).decode()[:10]

class SharePasteService:    
    def execute(self, expired_at, content, user):
        return Paste.objects.create(expired_at=expired_at, 
                                    content=content, user=user, 
                                    short_url=self.generate_shorten_url(
                                            content, user.pk if user else randint(1, 10 ** 10)
                                        ))

    def generate_shorten_url(self, content, user_id):
        unique_content = (f"{content}:{user_id}"
                            f":{timezone.now().microsecond}")
        return generate_random_hash(unique_content)
        
