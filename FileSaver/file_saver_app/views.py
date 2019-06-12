from rest_framework import viewsets
from . import models
from . import serializers

class FileUploadViewset(viewsets.ModelViewSet):
    queryset=models.FileUpload.objects.all()
    serializer_class=serializers.FileUploadSerializer
    
