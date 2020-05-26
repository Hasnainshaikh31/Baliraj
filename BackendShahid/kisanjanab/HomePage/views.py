from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse, redirect
from .models import Supplier
from .forms import SupplierLogInForm

# Create your views here.

def home(request, *args, **kwargs):
    if(request.method == "POST"):
        supplierLogInForm = SupplierLogInForm(request.POST)
        if (supplierLogInForm.is_valid()):
            print(supplierLogInForm.cleaned_data)
            response = redirect('/Supplier')
            return response
    else:
        supplierLogInForm = SupplierLogInForm()
        context = {'supplierLoginForm' : supplierLogInForm}
        return render(request, 'HomeTwo.html', context)

def supplierSignIn(request, *args, **kwargs):
    print('Insdide Method')
    return render(request, '/Supplier', {})