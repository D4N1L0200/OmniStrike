import os
import uuid
from . import CardType
from django.db import models  # type: ignore
from django.utils.text import slugify  # type: ignore


def rename_card_image(instance: models.Model, filename: str) -> str:
    assert isinstance(instance, Card)

    # ext = os.path.splitext(filename)[1].lower()  # e.g. ".jpg"
    ext = ".jpg"

    name_slug = slugify(
        instance.name
    )  # "Velociraptor Tracker" → "velociraptor-tracker"

    unique_id = uuid.uuid4().hex[:8]

    new_filename = f"{name_slug}-{unique_id}{ext}"

    return f"cards/{new_filename}"


class Card(models.Model):
    name = models.CharField(null=False, max_length=100)
    card_type = models.ForeignKey(CardType, on_delete=models.PROTECT)
    subtype = models.CharField(max_length=100, blank=True)

    attack = models.PositiveIntegerField(default=0)
    hp = models.PositiveIntegerField(default=0)

    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        # unique_together = ("card_set", "number_set")

    def __str__(self):
        return f"{self.name} ({self.card_type.name} - {self.subtype})"

    # def is_creature(self):
    #     return self.card_type.name.lower() == "creature"

    # def is_energy_source(self):
    #     return self.card_type.name.lower() in ["land", "energy source"]

    # def is_skill(self):
    #     return self.card_type.name.lower() == "skill"

    # def display_stats(self):
    #     if self.attack is not None and self.hp is not None:
    #         return f"{self.attack}/{self.hp}"
    #     return "-"
