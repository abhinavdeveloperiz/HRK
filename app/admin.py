from django.contrib import admin
from .models import student_gallery, office_gallery,Service, Head,Testimonial
# Register your models here.
admin.site.register(student_gallery)
admin.site.register(office_gallery)
admin.site.register(Service)
admin.site.register(Head)
admin.site.register(Testimonial)