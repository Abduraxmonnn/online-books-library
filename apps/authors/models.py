from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Name: {self.name} Created Date: {self.created_date}"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
