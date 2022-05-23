from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        roll = request.POST.get('roll')
        phone = request.POST.get('phone')
        dropdown = request.POST.get('dropdown')
        subject = request.POST.get('subject')

        contact.name = name
        contact.email = email
        contact.roll = roll
        contact.phone = phone
        contact.dropdown = dropdown
        contact.subject = subject
        contact.save()
        return HttpResponse("<h1> THANKS FOR CONTACT US </h1>")

    return render(request, 'index.html')
