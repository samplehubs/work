from django.views.decorators.csrf import csrf_exempt
from requests import request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from random import randint
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

@csrf_exempt
@api_view(['POST'])

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    def get_queryset(self,request):
        max_price = self.request.GET.get('max_price')
        min_price = self.request.GET.get('min_price')
        sort = self.request.GET.get('sort')
        keyword = self.request.GET.get('keyword')
        return Product.objects.filter_products(keyword, sort, min_price, max_price)

    
class RelatedProductView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, id, *args, **kwargs):
        product_id = id  # request.data.get("product_id")
        print(id)
        if not product_id:
            return Response({"error": "Product Id Not Found"}, status=HTTP_404_NOT_FOUND)
            product = get_object_or_404(Product, id=product_id)
            ProductModel.objects.filter(id=id).delete()
            products_serialized = ProductSerializer(
            product.get_related_products(), many=True, context={'request': request})
            return Response(products_serialized.data)

    
