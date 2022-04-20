from rest_framework import generics
from .serializers import ContactSerializer
from .models import Contact

from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
import json

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ContactSerializer # tell django what serializer to use

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all().order_by('id')
    serializer_class = ContactSerializer

# defines the functions
def post(self, request, *args, **kwargs):
    file = request.data['file']
    image = Contact.objects.create(image=file)
    return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)