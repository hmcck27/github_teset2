from .models import Item, Brand
from django.shortcuts import render

def item_list(request):
    qs = Item.objects.all()
    q = request.GET.get('q','')
    if q :
        qs = qs.filter(message__icontains = q)
    return render(request, 'items/item_list.html', {
                'item_list' : qs,
                'q' : q,
    })

def brand_list(request):
    qs = Brand.objects.all()
    q = request.GET.get('q','')
    if q :
        qs = qs.filter(message__icontains = q)
    return render(request, 'items/item_list.html', {
                'item_list' : qs,
                'q' : q,
    })
# Create your views here.
