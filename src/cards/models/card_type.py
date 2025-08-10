from django.db import models  # type: ignore


class CardType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
