from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import format_html

from .models import Image


@admin.register(Image)
class CustomUserAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'get_image', 'order')

    def get_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" '
                           f'style="width: 10%; height: 10%;" />')

    get_image.allow_tags = True
    get_image.short_description = "Image"
