from django.db import models
from django.core.exceptions import ValidationError

class Product(models.Model):
    ...

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean() 
        super().save(*args, **kwargs)