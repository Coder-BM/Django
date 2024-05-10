from django.contrib import admin
from .models import Product,Doctor,Appointment,ListProducts,DealDetails,DoctorVisit
from django.utils.html import format_html

    

class New_Admin(admin.ModelAdmin):
    list_display = ['First_name', 'Last_name', 'Email', 'Date_of_joining', 'status']

    def First_name(self,obj):
        return obj.user.first_name
    def Last_name(self,obj):
        return obj.user.last_name
    def Email(self,obj):
        return obj.user.email
    def Date_of_joining(self,obj):
        return obj.user.date_joined
    def status(self,obj):
        return obj.user.is_active

class New_Admin_Product(admin.ModelAdmin):
    list_display = ['Product_name', 'company_name', 'product_image', 'price', 'entered_by']
    
    def product_image(self,obj):
        return format_html("<img src = {} width = '90' height='90'>",obj.image.url)
    
class New_Admin_Doctor(admin.ModelAdmin):
    list_display = ['doc_name','doc_spec','doc_contact','doc_location','entered_by']

class New_Admin_Appointment(admin.ModelAdmin):
    list_display = ['Doctor_name','Booking_schedule','Booking_time','entered_by']

class New_Admin_ProductList(admin.ModelAdmin):
    list_display = ['Sr_No','Products_Name','Company_Name','Product_Image','Product_Price','Entered_By']

    def Sr_No(self,obj):
        return obj.user_name.id
    def Products_Name(self,obj):
        return obj.user_name.Product_name
    def Company_Name(self,obj):
        return obj.user_name.company_name
    def Product_Image(self,obj):
        return format_html("<img src = {} width = '90' height='90'>",obj.user_name.image.url)
    def Product_Price(self,obj):
        return obj.user_name.price
    def Entered_By(self,obj):
        return obj.user_name.entered_by
    
class New_Admin_Schedule(admin.ModelAdmin):
    list_display = ['Sr_No','Doctor_Name','Date_Of_Meeting','Time']
    list_filter = ['Date_Selector__entered_by']


    def Sr_No(self,obj):
        return obj.Date_Selector.id
    def Doctor_Name(self,obj):
        return obj.Date_Selector.Doctor_name
    def Date_Of_Meeting(self,obj):
        return obj.Date_Selector.Booking_schedule
    def Time(self,obj):
        return obj.Date_Selector.Booking_time
    
    
class New_Admin_Deal(admin.ModelAdmin):
    list_display = ['Doc_name','Prod_name','Quantity_Ordered','Date_of_order','entered_by']


# Register your models here.


admin.site.register(Product,New_Admin_Product)
admin.site.register(Doctor,New_Admin_Doctor)
admin.site.register(Appointment,New_Admin_Appointment)
admin.site.register(ListProducts,New_Admin_ProductList)

admin.site.register(DealDetails,New_Admin_Deal)
admin.site.register(DoctorVisit)

# admin.site.register(Employee2,New_Admin)
# admin.site.register(User)
