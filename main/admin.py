from django.contrib import admin
from .models import recognition

# Register your models here.
class RecognitionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Recognising:",{"fields": ["rec_title"]}),
        ("Reconising with:",{"fields": ["rec_subtitle"]}),
        ("Recognition Description",{"fields": ["rec_content"]}),
        ("Recognition Category",{"fields": ["rec_type"]}),
        ("Recognition Image",{"fields": ["rec_img"]}),
    ]

admin.site.register(recognition, RecognitionAdmin)
