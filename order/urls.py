from django.urls import path 
from . import views 

app_name = 'order'

urlpatterns = [
    path('create/',views.create_order, name='create_order'),
    path('invoice/<int:order_id>/pdf/',views.invoice,name='invoice')
    
]