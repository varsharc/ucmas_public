from django.contrib import admin
from .models import section

# Register your models here.
class SectionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title",{"fields": ["section_title"]}),
        ("Content",{"fields": ["section_body"]})
    ]

admin.site.register(section, SectionAdmin)
