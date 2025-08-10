from .models import *  # type: ignore
from django.contrib import admin  # type: ignore
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin  # type: ignore


class EnergyCostInline(admin.TabularInline):  # or admin.StackedInline
    model = EnergyCost
    extra = 0


class CardPrintInlineForCard(admin.TabularInline):
    model = CardPrint
    extra = 0


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "card_type",
        "subtype",
        "display_costs",
    )
    search_fields = ("name", "card_type__name", "subtype")
    inlines = [EnergyCostInline, CardPrintInlineForCard]

    # list_filter = ("card_set",)
    # ordering = ("card_set", "number_set")

    def display_costs(self, obj) -> str:
        return ", ".join(
            f"{cost.amount}{cost.energy_type.char}" for cost in obj.costs.all()
        )

    display_costs.short_description = "Energy Costs"  # type: ignore


class CardPrintInlineForCardSet(SortableInlineAdminMixin, admin.TabularInline):
    model = CardPrint
    extra = 0
    fields = ("card", "print_type", "print_palette")
    ordering = ["number_set"]


@admin.register(CardSet)
class CardSetAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ("name", "code", "release_date")
    inlines = [CardPrintInlineForCardSet]


@admin.register(CardPrint)
class CardPrintAdmin(admin.ModelAdmin):
    list_display = (
        "card",
        "print_type",
        "print_palette",
        "card_set",
    )
    search_fields = (
        "card__name",
        "card_set__name",
        "print_type__name",
        "print_palette__name",
    )


admin.site.register(CardType)
admin.site.register(EnergyType)
admin.site.register(EnergyCost)
admin.site.register(PrintType)
admin.site.register(PrintPalette)
