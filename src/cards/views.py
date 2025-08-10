from django.db.models import Q  # type: ignore
from .models import CardPrint, Card  # type: ignore
from django.shortcuts import render, get_object_or_404  # type: ignore


def home(request):
    return render(request, "home.html")


def cards(request):
    query = request.GET.get("search", "").strip()

    card_prints = CardPrint.objects.select_related("card_set", "card").order_by(
        "card_set__name", "number_set"
    )

    if query:
        card_prints = card_prints.filter(
            Q(card__name__icontains=query)
            | Q(card__description__icontains=query)
            | Q(card__subtype__icontains=query)
            | Q(card__card_type__name__icontains=query)
            | Q(card_set__name__icontains=query)
            | Q(card_set__code__icontains=query)
            | Q(print_type__name__icontains=query)
            | Q(print_palette__name__icontains=query)
        )

        """
        
        number_set
        card
        - name +
        - description +
        - attack
        - hp
        - subtype + 
        - card_type
          - name +
        card_set
        - name +
        - release_date
        - code +
        print_type
        - name + 
        print_palette
        - name +
        
        """

    return render(
        request,
        "cards/cards.html",
        {
            "card_prints": card_prints,
            "query": query,
        },
    )


def card_detail(request, id):
    card_print = get_object_or_404(CardPrint, pk=id)
    return render(request, "cards/card_detail.html", {"print": card_print})
