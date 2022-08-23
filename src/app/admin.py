from django.contrib import admin
from .models import Paste

# Register your models here.
class PasteAdmin(admin.ModelAdmin):
    list_display = ('short_url', 'expired_at', 'created_at', 'user', 'is_deleted')
    exclude = ('deleted_at', )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(Paste, PasteAdmin)