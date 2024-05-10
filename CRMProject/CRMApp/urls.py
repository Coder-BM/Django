from django.urls import path

from CRMApp.views import logout

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    
    path("",views.login_page,name='/'),
    path("forgot-password",views.forgot_pass,name='forgot-password'),
    path("sent-email",views.send_email,name='sent_email'),
    path("Terms&Conditions",views.terms,name='Terms&Conditions'),
    path("Privacy-Policy",views.policy,name='Privacy-Policy'),
    path('User-Dashboard',views.user_dashboard,name='User-Dashboard'),

    
    # For product
    path("add-product",views.add_product,name='add-product'),
    path('view-product',views.view_product,name='view-product'),
    path('delete-product/<int:id>',views.prod_delete,name='delete-product'),
    path('edit-product/<int:id>',views.prod_edit,name='edit-product'),

    #For Doctor
    path("add-doctor",views.add_doctor,name='add-doctor'),
    path('view-doctor',views.view_doctor,name='view-doctor'),
    path('delete-doctor/<int:id>',views.doc_delete,name='delete-doctor'),
    path('edit-doctor/<int:id>',views.doc_edit,name='edit-doctor'),

    #For Appointment
    path("appointment",views.appointment,name='appointment'),
    path('view-appointment',views.view_appointment,name='view-appointment'),
    path('delete-appointment/<int:id>',views.app_delete,name='delete-appointment'),
    path('edit-appointment/<int:id>',views.app_edit,name = 'edit-appointment'),


    #For Logout
    path('logout/',logout.as_view(),name='logout'),

    #for schedule
    path('schedule',views.schedule_list,name ='schedule'),

    #for deal
    path("deal",views.deals,name='deals'),
    path('view-deals',views.view_deal,name='view-deals'),
    path('delete-deal/<int:id>',views.deal_delete,name='delete-deal'),
    path('edit-deal/<int:id>',views.deal_edit,name='edit-deal'),

    # path("login",MyLogin.as_view(template_name='base/login.html'),name='login'),


]