from django.db import models

# Create your models here.
class section(models.Model):
    section_title = models.CharField(max_length=140)
    section_body = models.TextField(default="<text here>")
#    date = models.DateTimeField()

    def __str__(self):
        return self.section_title
