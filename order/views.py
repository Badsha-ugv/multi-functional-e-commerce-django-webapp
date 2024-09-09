from django.shortcuts import render, get_object_or_404
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
    

from django.conf import settings 
from django.http import HttpResponse
from django.template.loader import render_to_string 
from weasyprint import HTML 

def invoice(request,order_id):
    
    order = get_object_or_404(Order, id=order_id)
    html_string = render_to_string('order/pdf.html',{'order':order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename=invoice_{order_id}.pdf'
    HTML(string=html_string).write_pdf(response)
    
    # html = render_to_string('order/pdf.html',{'order':order})

    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'filename= order_{order_id}.pdf'
    # weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS])

    return response 

