from django.db import models


class UploadedDocs(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    extracted_text = models.TextField()
    upload_at = models.DateTimeField(auto_now_add=True)