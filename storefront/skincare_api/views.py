from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product

from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
import json

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ProductSerializer # tell django what serializer to use

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

# defines the functions
def post(self, request, *args, **kwargs):
    file = request.data['file']
    image = Product.objects.create(image=file)
    return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)