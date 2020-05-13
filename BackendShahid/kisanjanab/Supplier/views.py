from django.shortcuts import render
from .models import Supplier 

# Create your views here.

def showSupplier(request, *args,**kwargs):
    return render(request, 'SupplierProfile.html')