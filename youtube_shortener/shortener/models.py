# models.py
from django.db import models
import random
import string

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()
        super().save(*args, **kwargs)

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(6))
        while ShortenedURL.objects.filter(short_url=short_url).exists():
            short_url = ''.join(random.choice(characters) for _ in range(6))
        return short_url
