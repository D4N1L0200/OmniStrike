from django.urls import path  # type: ignore
from . import views

urlpatterns = [
    path("", views.home_redirect, name="index"),
    path("cards", views.cards, name="cards"),
    path("card/<int:id>/", views.card_detail, name="card_detail"),
    # path('detail/<int:id>/', views.detail, name='detail'),
    # path('create/', views.create, name='create'),
    # path('update/<int:id>/', views.update, name='update'),
    # path('delete/<int:id>/', views.delete, name='delete'),
]
