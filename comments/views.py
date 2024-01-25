from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CommentForm


@login_required
def add_comment(request):
    """ Add a comments to the store """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only store owners can do that.')
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





