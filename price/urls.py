
from django.urls import path
from .views import list_products,create_product,update_product,delete_product


urlpatterns = [
    
    # path('price',price),
    path('',list_products),
    path('create',create_product,name='create_product'),
    path('update/<int:id>',update_product,name='update_product'),
    path('delete/<int:id>',delete_product,name='delete_product')
    
    


  
]