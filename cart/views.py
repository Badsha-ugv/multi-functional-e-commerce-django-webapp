from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST


from .cart import Cart
from shop.models import Product 
from .forms import CartAddForm

# Create your views here.
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddForm(request.POST)

    if form.is_valid():
        print('form is valid')
        cd = form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'],update_quantity=cd['update'])
        return redirect('cart:cart_details')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_details')


def cart_details(request):
    print('method is called')
    cart = Cart(request)
    for item in cart:
        item['update_quantity'] = CartAddForm(initial={'quantity': item['quantity'],'update': True})
    return render(request,'cart/cart_details.html',{'cart':cart})

