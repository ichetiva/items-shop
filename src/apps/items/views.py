import stripe
from django.views.generic import ListView, DetailView, TemplateView
from django.http import JsonResponse
from django.conf import settings
from django.urls import reverse_lazy

from .models import Item, ItemPrice


class ListItemsView(ListView):
    template_name = 'items/items.html'
    context_object_name = 'items'
    queryset = Item.objects.all()

    def get_context_data(self, **kwargs):
        kwargs.update({'home_page': True})
        return super().get_context_data(**kwargs)


class ItemView(DetailView):
    template_name = 'items/item.html'
    context_object_name = 'item'
    queryset = Item.objects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prices'] = ItemPrice.objects.filter(item=context['item'])
        return context


class GetStripeSessionView(DetailView):
    queryset = Item.objects
    
    def get(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        item = self.get_object()
        price = ItemPrice.objects.get(item=item, currency=self.kwargs.get('currency'))
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': price.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': price.price * 100,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=settings.DOMAIN + 'success',
            cancel_url=settings.DOMAIN + 'cancelled'
        )
        return JsonResponse(data={'session_id': session['id']})


class SuccessPurchaseView(TemplateView):
    template_name = 'items/success_purchase.html'


class CancelledPurchaseView(TemplateView):
    template_name = 'items/cancelled_purchase.html'
