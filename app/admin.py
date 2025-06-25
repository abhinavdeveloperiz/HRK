from django.contrib import admin
from django.utils.html import format_html
from .models import student_gallery, office_gallery, Service, Head, Testimonial

# ======================
# Utility: Thumbnail Display
# ======================
def thumbnail(obj):
    if obj.image:
        return format_html('<img src="{}" width="100" style="border-radius: 8px;" />', obj.image.url)
    return "No Image"

thumbnail.short_description = 'Preview'


# ======================
# Admin Classes
# ======================

@admin.register(student_gallery)
class StudentGalleryAdmin(admin.ModelAdmin):
    list_display = ['id', thumbnail]

@admin.register(office_gallery)
class OfficeGalleryAdmin(admin.ModelAdmin):
    list_display = ['id', thumbnail]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'fees', 'level', 'created_at']
    readonly_fields = ['created_at']
    list_filter = ['type', 'level']
    search_fields = ['title', 'description']

@admin.register(Head)
class HeadAdmin(admin.ModelAdmin):
    def left_Carosel(self, obj):
        return format_html('<img src="{}" width="80"/>', obj.left.url if obj.left else "")
    
    def right_carosel(self, obj):
        return format_html('<img src="{}" width="80"/>', obj.right.url if obj.right else "")

    def Home_image(self, obj):
        return format_html('<img src="{}" width="80"/>', obj.image.url if obj.image else "")

    list_display = ['id', 'Home_image', 'left_Carosel', 'right_carosel']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" style="border-radius: 30px;" />', obj.image.url)
        return "No Image"

    list_display = ['name', 'image_preview', 'description']
