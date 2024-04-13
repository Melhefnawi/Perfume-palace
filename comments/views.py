from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Review
from .forms import ReviewForm
from .forms import ContactForm
from products.models import Product, Category


@login_required
def add_comment(request):
    """ Add a comments to the store """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only authenticated can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            messages.success(request, 'Successfully added your comment!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add your comment form is unvalid.')
    else:
        form = CommentForm()

    template = 'comments/add_comments.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review_detail.html', {'review': review})

@login_required
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.save()
            messages.success(request, 'Successfully added your review!')
            return redirect(reverse('home'))
    else:
        form = ReviewForm()
    return render(request, 'review/create_review.html', {'form': form})

@login_required
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully sent your request!')
            return redirect('home')  
    else:
        form = ContactForm()
    return render(request, 'contact/contact_us.html', {'form': form})

@login_required
def show_review(request):

    products = Product.objects.all()
    reviews = Review.objects.all()

    context = {
        'products': products,
        'reviews' : reviews,
        
    }


    return render(request, 'show_review/show_rev.html', context)


@login_required
def review_details(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    review_exists = Review.objects.filter(item=product).exists()

    if review_exists:

        review = Review.objects.filter(item=product)

        context = {
            'product': product,
            'review': review,
        }
    else:

        context = {
            'product': product,
        }


    return render(request, 'show_review/rev_details.html', context)

