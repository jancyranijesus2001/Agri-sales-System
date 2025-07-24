from django.shortcuts import render
from store.models.product import ProductPriceHistory
from django.utils.timezone import now

def product_list(request):
    today = now().date()
    
    # Get only products that have price history for today
    today_prices = ProductPriceHistory.objects.filter(date=today).order_by('-date')

    context = {
        'today_prices': today_prices
    }
    return render(request, 'products.html', context)
