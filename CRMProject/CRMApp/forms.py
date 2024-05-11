from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product,Doctor,Appointment,DealDetails
from datetime import date
from django.core.validators import MinValueValidator
 

class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Product_name','company_name','image','price']

    price = forms.FloatField(widget=forms.NumberInput(attrs={'type':'number'}))

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['doc_name','doc_spec','doc_contact','doc_location']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['Doctor_name','Booking_schedule','Booking_time']

    Booking_schedule =forms.DateField(
                                    required=True,
                                    widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'})
    )
    Booking_time = forms.TimeField(required=True,
                                       widget=forms.TimeInput(attrs={'placeholder': 'HH-MM-SS'}))
    
class ScheduleForm(forms.Form):
    date_select = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
class DealsForm(forms.ModelForm):

    class Meta:
        model = DealDetails
        fields = ['Doc_name','Prod_name','Quantity_Ordered','Date_of_order']

    Quantity_Ordered = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'number'}))
    Date_of_order = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
