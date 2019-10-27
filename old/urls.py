
from django.urls import path
from .views import  hotel_image_view,success,display_hotel_images

from django.conf import settings
urlpatterns = [
    
    # path('yuri',views.yuri)
    path('hotel', hotel_image_view,name='image_upload'),
    path('success',success,name='success'),
    path('images',display_hotel_images,name='hotel_images')


  
]