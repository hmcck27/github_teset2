from django.shortcuts import render
from .models import Review
# Create your views here.

def review_list(request):
    qs = Review.objects.all()
    q = request.GET.get('q','')
    if q :
        qs = qs.filter(message__icontains = q)
    return render(request, 'posts/review_list.html', {
                'review_list' : qs,
                'q' : q,
    })