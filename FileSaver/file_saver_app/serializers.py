from rest_framework import serializers
from . import models

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.FileUpload
        fields=('id','title','file','pub_date')
