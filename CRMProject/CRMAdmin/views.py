from django.shortcuts import render,redirect

from django.contrib.auth.views import LoginView,LogoutView

from django.contrib.auth import update_session_auth_hash

from django.urls import reverse_lazy

from django.contrib import messages

from CRMApp.models import Product,Doctor,Appointment,DealDetails,DoctorVisit,User

from CRMApp.forms import ProductFrom

from .forms import ProductFromAdmin,UserForm,UserUpdateForm,EmployeeForm,DealForm,DoctorVisitForm

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required
def djadmin(request):
    pro = Product.objects.all().count()
    doc = Doctor.objects.all().count()
    use = User.objects.all().count()
    app = Appointment.objects.all().count()
    deal = DealDetails.objects.all().count()
    d = {'objects':pro,'d_objects':doc,'u_objects':use,'a_objects':app,'deal_objects':deal}
    return render(request,"CRMAdmin/admin_dashboard.html",d)

class logout(LogoutView):
    def dispatch(self, request):
        user = request.user
        messages.success(request,"Thank you"+" " + str(user) +"."+"You have Logged out Successfully" )
        return super().dispatch(request)
    def get_next_page(self):
        return reverse_lazy('/')
    


#user

def add_user(request):
    if request.method == "GET":
        pf = UserForm()
        return render(request,"CRMAdmin/add_user.html",{'pf':pf})
    
    if request.method == "POST":
        pf = UserForm(request.POST)
        if pf.is_valid():
            us = pf.save(commit=False)
            us_exist = User.objects.filter(username = us.username).exists()

            if us_exist:
                # messages.error(request,"User Already Exist!!")
                return render(request,"CRMAdmin/add_user.html",{'pf':pf})
            else:
                us.save()
                messages.success(request,"User Added Successfully!!!")
                return redirect(view_user)
        else:
            messages.error(request,"Some Error!!!")
            return render(request,'CRMAdmin/add_user.html',{'pf':pf})
        
def view_user(request):
    b = User.objects.all()
    d = {'objects':b}
    return render(request,"CRMAdmin/view_user.html",d)

def delete_user(request,id):
    a = User.objects.get(id=id)
    a.delete()
    messages.success(request,"User Deleted Successfully!!")
    return redirect(view_user)      

def edit_user(request,id):
    a = User.objects.get(id=id)
    if request.method =="POST":
        pf = UserUpdateForm(request.POST,instance=a)
        if pf.is_valid():
            pf.save()
            messages.success(request,"User Details Edited Successfully!!")
            return redirect(view_user)
        else:
            messages.error(request, "Some Error!!")
            return render(request,'CRMAdmin/edit_user.html',{'pf':pf})
    else:
        pf = UserUpdateForm(instance=a)
        return render(request,'CRMAdmin/edit_user.html',{'pf':pf})
    

#Product
# @login_required
def add_product_admin(request):
    if request.method == "GET":
        pf = ProductFromAdmin()
        return render(request,"CRMAdmin/add_product.html",{'pf':pf})
    
    if request.method=="POST":
        pf = ProductFromAdmin(request.POST,request.FILES)
        if pf.is_valid():
            product = pf.save()
            product_exist = Product.objects.filter(Product_name = product.Product_name,entered_by = request.user).exists()

            if product_exist:
                messages.warning(request,"Product Already Added!!")
                return render(request,"CRMAdmin/add_product.html",{'pf':pf})
            else:
                product.save()
                messages.success(request,"Product Added Successfully!!!")
                return redirect(view_all_product)
        else:
            messages.error(request,"Some Error")
            return render(request,"CRMAdmin/add_product.html",{'pf':pf})

def view_all_product(request):
    b = Product.objects.all()
    d = {'objects':b}
    return render(request,"CRMAdmin/add_product_display.html",d)

# def all_prod_delete(request,id):
#     a = Product.objects.get(id=id)
#     a.delete()
#     messages.success(request,"Product Deleted Successfully.")
#     return redirect(view_all_product)

# def all_prod_edit(request):
    a = Product.objects.all()
    if request.method == "POST":
        pf = ProductFromAdmin(request.POST,request.FILES,instance=a)
        if pf.is_valid():
            pf.save()
            messages.success(request,"Product Edited Successfully!!")
            return redirect(view_all_product)
        else:
            messages.error(request,"Some Error!!")
            return render(request,'CRMAdmin/edit_product.html',{'pf':pf})
    else:

        pf = ProductFromAdmin(instance=a)
        return render(request,'CRMAdmin/edit_product.html',{'pf':pf})

def prod_list(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            select = form.cleaned_data['employee']
            user = select.id
            products = Product.objects.filter(entered_by=user)
            return render (request,"CRMAdmin/product_list.html",{'products':products})
    else:
        form = EmployeeForm()
        return render(request,'CRMAdmin/product_list_form.html',{'form':form})
    

def deal_list(request):
    if request.method =="GET":
        form = DealForm()
        return render(request,'CRMAdmin/deal_list_form.html',{"form":form})
    
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            select = form.cleaned_data['employee']
            choose_month = int(form.cleaned_data['month'])
            user = select.id
            user_name = select.username
            deal_count = DealDetails.objects.filter(entered_by=user,Date_of_order__month = choose_month).count()
            deal = DealDetails.objects.filter(entered_by=user,Date_of_order__month = choose_month)
            
            return render(request,'CRMAdmin/deal_list.html',{"deal":deal,'deal_count':deal_count,'user_name':user_name,'choose_month':choose_month})
    
#Doctor

def doctor_list(request):
    if request.method == "GET":
        form = DoctorVisitForm()
        return render(request,'CRMAdmin/doctor_list_form.html',{'form':form})
    
    if request.method == "POST":
        form = DoctorVisitForm(request.POST)
        if form.is_valid():
            select_employee = form.cleaned_data['employee']
            select_month = int(form.cleaned_data['month'])
            user = select_employee.id
            user_name = select_employee.username
            appointment = Appointment.objects.filter(entered_by = user,Booking_schedule__month = select_month)
            appointment_count = appointment.count()
            
            return render (request,"CRMAdmin/doctor_list.html",
                           {'appointment':appointment,
                            'appointment_count':appointment_count,
                            'user_name':user_name,
                            'select_month':select_month})

