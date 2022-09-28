from rest_framework import routers, serializers, viewsets
from .models import * 

# create user

  
          
class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields=('__all__') 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=('__all__') 