from django.urls import path

from .views import (
    ListItemsView, ItemView, GetStripeSessionView, SuccessPurchaseView, CancelledPurchaseView
)

urlpatterns = [
    path('', ListItemsView.as_view(), name='items'),
    path('item/<int:pk>/', ItemView.as_view(), name='item'),
    path('buy/<int:pk>/<currency>/', GetStripeSessionView.as_view(), name='buy'),
    path('success/', SuccessPurchaseView.as_view(), name='success_purchase'),
    path('cancelled/', CancelledPurchaseView.as_view(), name='cancelled_purchase'),
]
