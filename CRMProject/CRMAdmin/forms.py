from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from CRMApp.models import Product,Doctor,Appointment,DealDetails



class ProductFromAdmin(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Product_name','company_name','image','price','entered_by']

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','is_active','is_superuser','date_joined','last_login']
    
    username = forms.CharField(max_length=100, 
                               required=True, 
                               widget=forms.TextInput())
    
    email = forms.EmailField(max_length=100, 
                                required=True, 
                                widget=forms.TextInput())
    
    first_name = forms.CharField(max_length=100, 
                                required=True, 
                                widget=forms.TextInput())
    
    last_name = forms.CharField(max_length=100, 
                                required=True, 
                                widget=forms.TextInput())
   
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser', 'date_joined']

    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    email = forms.EmailField(max_length=100, required=True, widget=forms.TextInput())
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput())

class EmployeeForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=User.objects.all(),empty_label="Select User")

class DealForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=User.objects.all(),empty_label="Select User")
    month = forms.ChoiceField(choices=[(i,i) for i in range(1,13)])

class DoctorVisitForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=User.objects.all(),empty_label='Select User')
    month = forms.ChoiceField(choices=[(i,i) for i in range(1,13)])