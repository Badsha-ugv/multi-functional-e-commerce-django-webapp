from django.shortcuts import render
from django.http import HttpResponse

from .models import Order, OrderItem 
from .forms import OrderForm
from cart.cart import Cart 


def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            print('order',form)
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
        
            cart.clear()
        
            return render(request,'order/order_done.html',{'order':order})
        else:
            print('form error ',form.errors)
        # return HttpResponse('something went wrong')
    else:
        form = OrderForm()
        return render(request,'order/create_order.html',{'form':form,'cart':cart})
    
