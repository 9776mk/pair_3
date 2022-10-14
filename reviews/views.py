from django.shortcuts import render, redirect
from .models import Reviews
from .forms import ReviewsForm


def index(request):
    return render(request, 'reviews/index.html')


# Create your views here.
def create(request):
    if request.method == 'POST':
        # DB에 저장하는 로직
        review_form = ReviewsForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:index')
    else: 
        review_form = ReviewsForm()
    context = {
        'review_form': review_form
    }
    return render(request, 'reviews/create.html', context=context)