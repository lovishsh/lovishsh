from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Product
from .models import Contact
from .models import Order
 

# Register your models here.
 
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
 
 
