from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=255, null=True)
    content_type = models.CharField(max_length=255, null=True)
    file = models.FileField(upload_to='files/images/%Y/%m', null=True)
    uid = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name or f'id={self.id}'
