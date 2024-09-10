from django.contrib import admin
from .models import Order, OrderItem 
from django.urls import reverse
from django.utils.html import format_html 


class OrderItemInline(admin.TabularInline):
    model = OrderItem 
    raw_id_fields = ['product']




class OrderAdmin(admin.ModelAdmin):
    def invoice_(obj):
        return format_html('<a href="{}">PDF</a>'.format(reverse('order:invoice', args=[obj.id])))

    invoice_.allow_tags = True
    invoice_.short_description = "Invoice"    

    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'post_code', 'city', 'paid', 'created',invoice_]
    list_display_links = ('first_name', 'last_name', 'email')
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

    

    
admin.site.register(Order, OrderAdmin)