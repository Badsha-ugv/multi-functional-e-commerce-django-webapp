from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddForm
from .models import Category, Product


def product_list(request, category_slug = None):
    category = None 
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    context = {
        'categories':categories,
        'products':products,
        'category':category
    }
    print(category)
    return render(request,'shop/product/list.html',context)

    
def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    form = CartAddForm()

    return render(request,'shop/product/details.html',{'product':product,'form':form})

