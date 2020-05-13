from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from .models import Supplier
from .forms import SupplierLogInForm

# Create your views here.

def home(request, *args, **kwargs):
    if(request.method == "POST"):
        supplierLogInForm = SupplierLogInForm(request.POST)
        if (supplierLogInForm.is_valid()):
            print(supplierLogInForm.cleaned_data)
    else:
        supplierLogInForm = SupplierLogInForm()
        context = {'supplierLoginForm' : supplierLogInForm}
        return render(request, 'HomeTwo.html', context)

def supplierSignIn(request, *args, **kwargs):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']

        Supplier.objects.create(
            username = username,
            password = password
        )

    return HttpResponse('')