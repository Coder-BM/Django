from django.urls import path

from CRMAdmin.views import logout



from . import views

urlpatterns = [

    path('djadmin/',views.djadmin,name='djadmin'),
    path('logout/',logout.as_view(),name='logout'),

    #For product
    path("add-product-admin",views.add_product_admin,name='add-product-admin'),
    path('view-all-product',views.view_all_product,name='view-all-product'),
    # path('delete-all-product/<int:id>',views.all_prod_delete,name='delete-all-product'),
    # path('edit-all-product',views.all_prod_edit,name='edit-all-product'),
    path('product_list', views.prod_list, name='product_list'),



    # For user
    path("add-user",views.add_user,name='add-user'),
    path('view-user',views.view_user,name='view-user'),
    path('delete-user/<int:id>',views.delete_user,name='delete-user'),
    path('edit-user/<int:id>',views.edit_user,name='edit-user'),
    


    #Deal
    path('deal_list', views.deal_list, name='deal_list'),

    #doctor

    path('doctor_list',views.doctor_list,name = 'doctor_list'),


]