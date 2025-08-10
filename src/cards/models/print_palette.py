from django.db import models  # type: ignore


class PrintPalette(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name
