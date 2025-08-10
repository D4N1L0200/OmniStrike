from django.db import models  # type: ignore
from .card import Card


class CardSet(models.Model):
    name = models.CharField(null=False, max_length=100)
    code = models.CharField(null=False, max_length=4, unique=True)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
