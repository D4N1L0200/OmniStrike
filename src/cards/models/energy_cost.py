from django.db import models  # type: ignore
from . import Card, EnergyType  # type: ignore


class EnergyCost(models.Model):
    card = models.ForeignKey(Card, related_name="costs", on_delete=models.PROTECT)
    energy_type = models.ForeignKey(EnergyType, on_delete=models.PROTECT, null=False)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.amount}{self.energy_type.char} for {self.card.name}"
