

# Create your models here.
import uuid
from django.db import models

class URL(models.Model):
    long_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = str(uuid.uuid4())[:6]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.long_url