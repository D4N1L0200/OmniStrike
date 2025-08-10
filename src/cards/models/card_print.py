import uuid
from django.db import models  # type: ignore
from . import Card, PrintType, PrintPalette
from django.utils.text import slugify  # type: ignore


def rename_card_image(instance: models.Model, filename: str) -> str:
    assert isinstance(instance, CardPrint)

    ext = ".jpg"

    name_slug = slugify(
        instance.card.name
    )  # "Velociraptor Tracker" → "velociraptor-tracker"

    unique_id = uuid.uuid4().hex[:8]

    new_filename = f"{name_slug}-{unique_id}{ext}"

    return f"cards/{new_filename}"


class CardPrint(models.Model):
    card = models.ForeignKey(Card, related_name="prints", on_delete=models.PROTECT)
    image = models.ImageField(
        null=False, default="no-photo.jpg", upload_to=rename_card_image
    )
    print_type = models.ForeignKey(PrintType, on_delete=models.PROTECT)
    print_palette = models.ForeignKey(
        PrintPalette,
        related_name="prints",
        on_delete=models.PROTECT,
    )

    card_set = models.ForeignKey(
        "CardSet",
        related_name="prints",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    number_set = models.PositiveIntegerField(blank=True, null=True)

    # class Meta:
    #     unique_together = ("card_set", "number_set")

    def save(self, *args, **kwargs):
        if self.number_set is None:
            max_number = (
                CardPrint.objects.filter(card_set=self.card_set).aggregate(
                    models.Max("number_set")
                )["number_set__max"]
                or 0
            )
            self.number_set = max_number + 1
        super().save(*args, **kwargs)

    def __str__(self):
        if self.card_set is None:
            set_name = "No Set"
        else:
            set_name = self.card_set.name
        return (
            f"{self.card.name} ({self.print_type.name}) - {set_name} #{self.number_set}"
        )
