from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import date
from django.core.validators import MinValueValidator


# Create your models here.


class Product(models.Model):
    Product_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    price = models.FloatField(validators=[MinValueValidator(0)])
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.entered_by)

class Doctor(models.Model):
    spec = (('Allergists/Immunologists','Allergists/Immunologists'),
            ('Anesthesiologists','Anesthesiologists'),
            ('Cardiologists','Cardiologists'),
            ('Colon and Rectal Surgeons','Colon and Rectal Surgeons'),
            ('Critical Care Medicine Specialists','Critical Care Medicine Specialists'),
            ('Dermatologists','Dermatologists'),
            ('Endocrinologists','Endocrinologists'),
            ('Family Physicians','Family Physicians'),
            ('Gastroenterologists','Gastroenterologists'),
            ('Gastroenterologists','Gastroenterologists'),
            ('Geriatric Medicine Specialists','Geriatric Medicine Specialists'),
            ('Hematologists','Hematologists'),
            ('Oncologists','Oncologists'),
            ('Ophthalmologists','Ophthalmologists'),
            ('Pathologists','Pathologists'),
            ('Pediatricians','Pediatricians'),
            ('Physiatrists','Physiatrists'),
            ('Plastic Surgeons','Plastic Surgeons'),
            ('Radiologists','Radiologists'),
            )
    doc_name = models.CharField(max_length=100)
    doc_spec = models.CharField(max_length=200,choices=spec)
    doc_contact = models.CharField(max_length=100)
    doc_location = models.CharField(max_length=100)
    entered_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    
    def __str__(self):
        return str(self.doc_name)


class Appointment(models.Model):
    Doctor_name = models.ForeignKey(Doctor,on_delete=models.CASCADE,blank=True,null=True)
    Booking_schedule = models.DateField()
    Booking_time = models.TimeField()
    entered_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return str(self.Booking_schedule)
    

class ListProducts(models.Model):
    user_name = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)


class DealDetails(models.Model):
    Doc_name = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True)
    Prod_name = models.CharField(max_length=100)
    Quantity_Ordered = models.IntegerField(validators=[MinValueValidator(0)])
    Date_of_order = models.DateField(default=date.today())
    entered_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    

    def __str__(self):
        return str(self.entered_by)

class DoctorVisit(models.Model):
    Date_Of_Visit = models.ForeignKey(DealDetails,on_delete=models.CASCADE,null=True,blank=True)
    entered_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)    


class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Token for {self.user.username}"
    
 