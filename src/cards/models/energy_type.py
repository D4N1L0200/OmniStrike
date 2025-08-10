from django.db import models  # type: ignore


class EnergyType(models.Model):
    name = models.CharField(max_length=16, unique=True)
    char = models.CharField(max_length=1, unique=True)

    def __str__(self):
        return f"{self.name} ({self.char})"
