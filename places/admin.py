from adminsortable2.admin import SortableStackedInline,  SortableAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(SortableStackedInline):
    model = Image
    fields = ['image', 'preview']
    readonly_fields = ["preview"]

    def preview(self, obj):
        return format_html(
            '<img src="{}" max-width="400px" max-height="300px"/>',
            obj.image.url
            )


@admin.register(Place)
class PostAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ['title']
    inlines = (ImageInline,)


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    autocomplete_fields = ['place']
    readonly_fields = ['preview']

    def preview(self, obj):
        return format_html(
            '<img src="{}" max-width="400px" max-height="300px" />',
            obj.image.url
            )
