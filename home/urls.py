from django.urls import path
from .import views

from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('Signin/', views.signin,name='Signin'),  
    path('register/', views.register, name='register'),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    path('api/product/', views.Production,name='Production'), 
    path('api/production/', views.Product,name='Product'), 


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)