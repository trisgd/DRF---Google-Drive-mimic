from django.db import models

class FileUpload(models.Model):
    title=models.CharField(max_length=100)
    file=models.FileField(blank=False, null=False)
    pub_date=models.DateTimeField(auto_now_add=True)
