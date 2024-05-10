from typing import Any
from django import http
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login,authenticate
from .forms import ProductFrom,DoctorForm,AppointmentForm,ScheduleForm,DealsForm
from django.contrib.auth.decorators import login_required
from .models import Product,Doctor,Appointment,DealDetails,PasswordResetToken
from datetime import datetime
from django import forms
from CRMAdmin.views import djadmin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
#to forgot password links.
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
# Create your views here.


def forgot_pass(request):
    return render(request,"base/Fgpwd.html")

# def send_email(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         if User.objects.filter(email=email).exists():
#             user = User.objects.get(email=email)
#             uid = urlsafe_base64_encode(force_bytes(user.pk))
#             token = default_token_generator.make_token(user)
#             PasswordResetToken.objects.create(user=user,token=token)
#             current_site=get_current_site(request)
#             reset_url = f"http://{current_site.domain}/reset-password/{uid}/{token}/"
#             subject = 'Password Reset Request'
#             message = render_to_string('base/password_reset_email.html',{'user':user,'reset_url':reset_url})
#             from_email = 'blavmir@gmail.com'
#             to_email = [email]
#             send_mail(subject,message,from_email,to_email)
#             messages.success(request,"Email sent successfully!!")
#             return render(request,'base/Fgpwd.html')
#         else:
#             messages.error(request,"Not a registered email id!!")
#     return render(request,'base/Fgpwd.html')

def send_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            PasswordResetToken.objects.create(user=user,token=token)
            current_site=get_current_site(request)
            subject = 'Password Reset Request'
            reset_url = f"http://{current_site.domain}/reset-password/{uid}/{token}/"  # Replace with your reset password URL
            html_content = render_to_string('base/password_reset_email.html', {'user': user, 'reset_url': reset_url})
            text_content = strip_tags(html_content)  # Strip HTML tags for plain text email
            email = EmailMultiAlternatives(subject, text_content, to=[email])
            email.attach_alternative(html_content, "text/html")  # Set HTML content
            email.send()
            messages.success(request, "Email sent successfully!!")
        else:
            messages.error(request, "Not a registered email id!!")
    
    return render(request, 'base/Fgpwd.html')

def terms(request):
    return render(request,"base/terms&conditions.html")

def policy(request):
    return render(request,"base/policy.html")

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"You have Logged in Successfully")

                if user.is_superuser:
                    return redirect(djadmin)
                else:
                    return redirect(user_dashboard)
            else:
                messages.error(request, "Incorrect Password!!")
        else:
            messages.error(request,'You have not been registered by the admin.Kindly contact them for the same')

    return render(request,"base/login.html")


class logout(LogoutView):
    def dispatch(self, request):
        user = request.user
        messages.success(request,"Thank you"+" " + str(user) +"."+"You have Logged out Successfully" )
        return super().dispatch(request)
    def get_next_page(self):
        return reverse_lazy('/')


#Product
# @login_required
def add_product(request):
    if request.method == "GET":
        pf = ProductFrom()
        return render(request,"base/add_product.html",{'pf':pf})
    
    if request.method=="POST":
        pf = ProductFrom(request.POST,request.FILES)
        if pf.is_valid():
            product = pf.save()
            product.entered_by = request.user
            product_exist = Product.objects.filter(Product_name = product.Product_name,entered_by = request.user).exists()
            
            if product_exist:
                messages.warning(request,"Product Already Added!!")
                return render(request,"base/add_product.html",{'pf':pf})
            else:
                product.save()
                messages.success(request,"Product Added Successfully!!!")
                return redirect(view_product)
        else:
            messages.error(request,"Some Error")
            return render(request,"base/add_product.html",{'pf':pf})

def view_product(request):
    user = request.user
    b = Product.objects.filter(entered_by = user)
    d = {'objects':b}
    return render(request,"base/add_product_display.html",d)

def prod_delete(request,id):
    a = Product.objects.get(id=id)
    a.delete()
    messages.success(request,"Product Deleted Successfully.")
    return redirect(view_product)

def prod_edit(request,id):
    a = Product.objects.get(id=id)
    if request.method == "POST":
        pf = ProductFrom(request.POST,request.FILES,instance=a)
        pf.save()
        messages.success(request,"Product Edited Successfully!!")
        return redirect(view_product)
    else:
        pf = ProductFrom(instance=a)
    return render(request,'base/edit_product.html',{'pf':pf})

#Doctor
def add_doctor(request):
    if request.method == "GET":
        pf = DoctorForm()
        return render(request,"base/add_doctor.html",{'pf':pf})
    
    if request.method=="POST":
        pf = DoctorForm(request.POST,request.FILES)
        if pf.is_valid():
            doctor = pf.save()
            doctor.entered_by_id = request.user.id
            doctor.save()
            messages.success(request,"Doctor Added Successfully!!!")
            return redirect(view_doctor)
        else:
            messages.error(request,"Some Error")
            return render(request,"base/add_doctor.html",{'pf':pf})


def view_doctor(request):
    user = request.user
    b = Doctor.objects.filter(entered_by = user)
    d = {'objects':b}
    return render(request,"base/add_doctor_display.html",d)

def doc_delete(request,id):
    a = Doctor.objects.get(id=id)
    a.delete()
    messages.success(request,"Doctor Deleted Successfully.")
    return redirect(view_doctor)

def doc_edit(request,id):
    a = Doctor.objects.get(id=id)
    if request.method == "POST":
        pf = DoctorForm(request.POST,request.FILES,instance=a)
        pf.save()
        messages.success(request,"Doctor details edited successfully!!")
        return redirect(view_doctor)
    else:
        pf = DoctorForm(instance=a)
        return render(request,"base/edit_doctor_details.html",{'pf':pf})

@login_required
def user_dashboard(request):
    user = request.user
    pro = Product.objects.filter(entered_by = user).count()
    doc = Doctor.objects.filter(entered_by = user).count()
    deal = DealDetails.objects.filter(entered_by = user).count()
    app = Appointment.objects.filter(entered_by = user).count()
    d = {'objects':pro,'d_objects':doc,'deal_objects':deal,'app_objects':app}
    return render(request,"base/user_dashboard.html",d)
    

# Appointment
def appointment(request):
    if request.method == "GET":
        pf = AppointmentForm()
        d = {'pf':pf}
        return render(request,"base/appointment.html",d)
    
    if request.method=="POST":
        pf = AppointmentForm(request.POST)
        if pf.is_valid():
            app = pf.save()
            app.entered_by_id = request.user.id
            # app.Doctor_name_id = request.Doctor.id
            app.save()
            messages.success(request,"Appointment Added Successfully!!!")
            return redirect(view_appointment)
        else:
            messages.error(request,"Some Error")
            return render(request,"base/appointment.html",d)


def view_appointment(request):
    user = request.user
    b = Appointment.objects.filter(entered_by = user)
    d = {'objects':b}
    return render(request,"base/appointment_display.html",d)


def app_delete(request,id):
    a = Appointment.objects.get(id=id)
    a.delete()
    messages.success(request,"Appointment Deleted Successfully.")
    return redirect(view_appointment)

def app_edit(request,id):
    a = Appointment.objects.get(id=id)
    if request.method == "POST":
        pf = AppointmentForm(request.POST,request.FILES,instance=a)
        pf.save()
        messages.success(request,"Appointment Details Edited Successfully!!")
        return redirect(view_appointment)
    else:
        pf = AppointmentForm(instance=a)
        return render(request,"base/edit_appointment.html",{'pf':pf})

# Schedule
#Ask Sir
#Error TypeError at /schedule
#fromisoformat: argument must be str
def schedule_list(request):
    if request.method =="GET":
        form = ScheduleForm()
        return render(request,"base/schedule_form.html",{'form':form})
    
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            selected_date = str(form.cleaned_data['date_select'])
            user = request.user
            final = Appointment.objects.filter(Booking_schedule = selected_date,entered_by=user)
            return render (request,"base/schedule_form_display.html",{'final':final,'user':user,'selected_date':selected_date})
        else:
            return render(request,"base/schedule_form.html",{'form':form})
        
# def schedule(request):
    
#     if request.method == "GET":
#         pf = ScheduleForm()
#         d = {'pf':pf}
#         return render(request,"base/schedule.html",d)
    
#     if request.method == "POST":
#         pf = ScheduleForm(request.POST)
#         if pf.is_valid():
#             # sch = pf.save()
#             select_date = pf.cleaned_data.get['Date_Selector']
#             user = request.user
#             # appointment = TodaysSchedule.objects.filter(Date_Selector__Booking_schedule=select_date,Date_Selector__entered_by =user)
#             appointments = Appointment.objects.filter(
#                 Booking_schedule=select_date, entered_by=user
#             ).order_by('Booking_time')
#             d = {'appointments':appointments,'select_date':select_date,'user':user}
#             return render(request,"base/schedule_doctor.html",d)
#         return render(request, "base/schedule.html", {'pf': pf})
#         # else:
#         #     messages.error(request,"Some Error")
#         #     d = {'pf':pf}
#         #     return render(request,"base/schedule.html",d)

# # def view_schedule(request):
# #     user = request.user
# #     if request.method == "GET":
# #         pf = ScheduleForm(request.GET)
# #         if pf.is_valid():
# #             select_date = pf.cleaned_data['Date_Selector']
# #             appointment = Appointment.objects.filter(Booking_schedule=select_date,entered_by =user)
# #             d = {'appointment':appointment,'select_date':select_date}
# #             return render(request,"base/schedule_doctor.html",d)
# #         else:
# #             pf = ScheduleForm()
# #             d = {'pf':pf}
# #             return render(request,"base/schedule_doctor.html",d)



#Deals

def deals(request):
    if request.method == "GET":
        pf = DealsForm()
        d = {'pf':pf}
        return render(request,"base/deal_details.html",d)
    
    if request.method=="POST":
        pf = DealsForm(request.POST)
        if pf.is_valid():
            de = pf.save()
            de.entered_by_id = request.user.id
            # app.Doctor_name_id = request.Doctor.id
            de.save()
            messages.success(request,"Deal Added Successfully!!!")
            return redirect(view_deal)
        else:
            messages.error(request,"Some Error")
            return render(request,"base/deal_details.html",d)
        
def view_deal(request):
    user = request.user
    b = DealDetails.objects.filter(entered_by = user)
    d = {'objects':b}
    return render(request,"base/deal_details_display.html",d)


def deal_delete(request,id):
    a = DealDetails.objects.get(id=id)
    a.delete()
    messages.success(request,"Deal Deleted Successfully.")
    return redirect(view_deal)

def deal_edit(request,id):
    a = DealDetails.objects.get(id=id)
    if request.method == 'POST':
        pf = DealsForm(request.POST,request.FILES,instance=a)
        pf.save()
        messages.success(request,"Deal Details Updated Successfully!!")
        return redirect(view_deal)
    else:
        pf = DealsForm(instance=a)
        return render(request,"base/edit_deal.html",{'pf':pf})
