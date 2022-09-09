from django.forms import ModelForm
from .models import Paste


class PasteForm(ModelForm):
    template_name = "bootstrap-form-field.html"

    class Meta:
        model = Paste
        fields = ["name", "content", "expired_at", "permanent_delete"]
