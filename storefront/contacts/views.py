from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from skincare_api.models import Contact
from django.shortcuts import redirect

# Create your views here.
def index(request):
    if request.method == "GET":
        contacts = Contact.objects.all()
        context = {
            'contacts': contacts
        }
        return render(request, 'contacts/index.html', context)
    elif request.method == "POST":
        print(request.POST)
        new_contact = Contact.objects.create(
            productName=request.POST["productName"],
            # image=request.POST["image"],
            brand=request.POST["brand"],
            price=request.POST["price"],
            benefits=request.POST["benefits"])
        return redirect('/contacts')

def new(request):
    return render(request, 'contacts/new.html')

def detail(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if request.method == "GET":
        context = {
            'contact': contact
        }
        return render(request, 'contacts/detail.html', context)
    elif request.method == "DELETE":
        contact.delete()
        return redirect("/contacts")
    elif request.method == "PUT":
        contact.productName = request.PUT["productName"]
        contact.brand = request.PUT["brand"]
        contact.price = request.PUT["price"]
        contact.benefits = request.PUT["benefits"]
        contact.save()
        return redirect('/contacts/'+contact_id)