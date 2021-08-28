from django.db import models

# Create your models here.

class TvShow(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __repr__(self):
        return f"{self.title} - {self.network} - {self.release_date}"
    def __str__(self):
        return f"{self.title} {self.description}"