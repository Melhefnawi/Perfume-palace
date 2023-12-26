from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ add quantity of a specific product """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag',{})

    if item_id in list(bag.keys()):
        bag[item_id]+= quantity
    else:
        bag[item_id]= quantity

    request.session['bag'] = bag   
    
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ adjust quantities of  product  in the bag """

    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag',{})

    if quantity > 0:
            bag[item_id] = quantity
    else:
            bag.pop(item_id)


    request.session['bag'] = bag   
    
    return redirect(reverse('view_bag'))   

def remove_from_bag(request, item_id):
    """ remove from bag  product """
    try:
        
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))  

    except Exception as e:
        return HttpResponse(status=500)  