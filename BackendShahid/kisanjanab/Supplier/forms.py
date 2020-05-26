from django import forms
from . import models

class SupplierProfileForm(forms.ModelForm):
    class Meta:
        model = models.Supplier
        fields = ("first_name", "middle_name", "last_name", "phone_number",
                  "mobile_number", "email", "email_optional", "address", 
                  "area_street", "city", "district", "taluka", "state",
                  "pincode", "designation")
        widgets = {
                'first_name' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'First Name'}),
                'middle_name' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Middle Name'}),
                'last_name' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Last Name'}),
                'designation' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Designation'}),
                'phone_number' : forms.NumberInput(attrs = {'class' : 'form-control', 'placeholder' : 'Phone Number'}),
                'mobile_number' : forms.NumberInput(attrs = {'class' : 'form-control', 'placeholder' : 'Mobile Number'}),
                'email' : forms.EmailInput(attrs = {'class' : 'form-control', 'placeholder' : 'Email'}),
                'email_optional' : forms.EmailInput(attrs = {'class' : 'form-control', 'placeholder' : 'Optional Email'}),
                'address' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Address'}),
                'area_street' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Area/Street'}),
                'city' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'City'}),
                'district' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'District'}),
                'taluka' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Taluka'}),
                'state' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'state'}),
                'pincode' : forms.NumberInput(attrs = {'class' : 'form-control', 'placeholder' : 'Pincode'}),
        }