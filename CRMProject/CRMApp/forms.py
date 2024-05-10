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
    # date_select = forms.ModelChoiceField(queryset=Appointment.objects.all(),empty_label="Select Date")
    date_select = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
class DealsForm(forms.ModelForm):
    # Quantity_Ordered = forms.IntegerField(validators=[MinValueValidator(0)], widget=forms.NumberInput(attrs={'type': 'number'}))
    # Date_of_order = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


    class Meta:
        model = DealDetails
        fields = ['Doc_name','Prod_name','Quantity_Ordered','Date_of_order']

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['Quantity_Ordered'].widget = forms.NumberInput(attrs={'type': 'number'})
        #     self.fields['Quantity_Ordered'].validators.append(MinValueValidator(0))
        #     self.fields['Date_of_order'].widget = forms.DateInput(attrs={'type': 'date'})
        # # widgets = {
        # #     'Quantity_Ordered': forms.NumberInput(attrs={'type': 'number'}),
        # #     'Date_of_order': forms.DateInput(attrs={'type': 'date'}),
        # # }
        # # validators = {
        # #     'Quantity_Ordered': [MinValueValidator(0)],
        # # }



    Quantity_Ordered = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'number'}))
    Date_of_order = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
