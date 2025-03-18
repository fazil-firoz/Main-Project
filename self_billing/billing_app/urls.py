"""self_billing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from billing_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login1',views.login1,name='login1'),
    path('logincode',views.logincode,name='logincode'),
    path('adddelivery',views.adddelivery,name='adddelivery'),
    path('add_security',views.add_security,name='add_security'),
    path('add_security_post',views.add_security_post,name='add_security_post'),
    path('adddeliverycode',views.adddeliverycode,name='adddeliverycode'),
    # path('adddnotification',views.adddnotification,name='adddnotification'),
    # path('addoffers',views.addoffers,name='addoffers'),
    path('add_stockmanager',views.add_stockmanager,name='add_stockmanager'),
    path('add_stock_manager_post', views.add_stock_manager_post, name='add_stock_manager_post'),
    # path('mngoffers', views.mngoffers, name='mngoffers'),

    path('adminhome',views.adminhome,name='adminhome'),
    path('managesalesman',views.managesalesman,name='managesalesman'),
    path('managestaff',views.managestaff,name='managestaff'),
    # path('offersadd', views.offersadd, name='offersadd'),
    path('sendnotification', views.sendnotification, name='sendnotification'),
    path('viewcomplates', views.viewcomplates, name='viewcomplates'),
    path('viewproduts', views.viewproduts, name='viewproduts'),
    path('viewpurchaseproduct', views.viewpurchaseproduct, name='viewpurchaseproduct'),
    path('viewpurchase', views.viewpurchase, name='viewpurchase'),
    path('viewraiting', views.viewraiting, name='viewraiting'),
    path('viewreply/<int:id>', views.viewreply, name='viewreply'),
    path('viewusers', views.viewusers, name='viewusers'),
    path('addproduct', views.addproduct, name='addproduct'),
    path('assign/<int:id>', views.assign, name='assign'),
    path('manageproduct', views.manageproduct, name='manageproduct'),
    path('staffhome', views.staffhome, name='staffhome'),
    path('viewcomplatesstaff', views.viewcomplatesstaff, name='viewcomplatesstaff'),
    path('viewdeliverystatus', views.viewdeliverystatus, name='viewdeliverystatus'),
    path('viewfeedback', views.viewfeedback, name='viewfeedback'),
    path('viewstock', views.viewstock, name='viewstock'),
    path('searchproducts', views.searchproducts, name='searchproducts'),
    path('viewnotification', views.viewnotification, name='viewnotification'),
    path('viewonlineorder', views.viewonlineorder, name='viewonlineorder'),
    path('viewfeedback', views.viewfeedback, name='viewfeedback'),
    path('viewproduct', views.viewproduct, name='viewproduct'),
    path('viewproductss', views.viewproductss, name='viewproductss'),
    path('orderscode', views.orderscode, name='orderscode'),
    path('viewproductsearch', views.viewproductsearch, name='viewproductsearch'),
    path('search_staff', views.search_staff, name='search_staff'),
    path('search_product', views.search_product, name='search_product'),
    path('edit_staff/<int:id>', views.edit_staff, name='edit_staff'),
    path('delete_staff/<int:id>', views.delete_staff, name='delete_staff'),
    path('delete_deliveryboy/<int:id>', views.delete_deliveryboy, name='delete_deliveryboy'),
    path('edit_stafff', views.edit_stafff, name='edit_stafff'),
    path('Editproduct/<int:id>', views.Editproduct, name='Editproduct'),
    path('edit_deliveryboy/<int:id>', views.edit_deliveryboy, name='edit_deliveryboy'),
    # path('delete_offers/<int:id>', views.delete_offers, name='delete_offers'),
    path('deleteproduct/<int:id>', views.deleteproduct, name='deleteproduct'),
    path('searchproduct', views.searchproduct, name='searchproduct'),
    path('addproduct', views.addproduct, name='addproduct'),
    path('addproductcode', views.addproductcode, name='addproductcode'),
    path('editproductcode', views.editproductcode, name='editproductcode'),
    path('editproductcodes', views.editproductcodes, name='editproductcodes'),
    # path('searchoffers', views.searchoffers, name='searchoffers'),
    path('logincode1', views.logincode1, name='logincode1'),
    path('registration', views.registration, name='registration'),
    path('view_product/<int:id>', views.view_product, name='view_product'),
    path('viewproductmore', views.viewproductmore, name='viewproductmore'),
    path('ordr_status', views.ordr_status, name='ordr_status'),
    path('viewmycart', views.viewmycart, name='viewmycart'),
    path('ordrprdctcard', views.ordrprdctcard, name='ordrprdctcard'),
    path('editstock/<int:id>', views.editstock, name='editstock'),
    path('orderfromcart/<int:id>', views.orderfromcart, name='orderfromcart'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('delete_noti/<int:id>', views.delete_noti, name='delete_noti'),
    path('vieworderstatus', views.vieworderstatus, name='vieworderstatus'),
    path('edit_deliveryboycode', views.edit_deliveryboycode, name='edit_deliveryboycode'),
    path('viewfeedback_admin', views.viewfeedback_admin, name='viewfeedback_admin'),
    path('viewreply_post', views.viewreply_post, name='viewreply_post'),
    path('assignorder', views.assignorder, name='assignorder'),
    path('viewdproducts/<int:id>', views.viewdproducts, name='viewdproducts'),
    path('addtocart', views.addtocart, name='addtocart'),
    path('logout', views.logout, name='logout'),
    path('ordrprdctcode', views.ordrprdctcode, name='ordrprdctcode'),
    path('ordrprdct', views.ordrprdct, name='ordrprdct'),
    path('ordrdtls/<int:id>', views.ordrdtls, name='ordrdtls'),
    path('view_item_ordr_status/<int:id>', views.view_item_ordr_status, name='view_item_ordr_status'),
    path('srchordr_products', views.srchordr_products, name='srchordr_products'),



    path('userGenerateBillamt', views.userGenerateBillamt, name='userGenerateBillamt'),
    path('userGenerateBill', views.userGenerateBill, name='userGenerateBill'),
    path('userAddToCart1', views.userAddToCart1, name='userAddToCart1'),
    path('select_product', views.select_product, name='select_product'),
    path('generateBill3', views.generateBill3, name='generateBill3'),
    path('finishBill', views.finishBill, name='finishBill'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('paymentfinish', views.paymentfinish, name='paymentfinish'),
    path('viewmyproductincard', views.viewmyproductincard, name='viewmyproductincard'),
    path('cancel_s_order', views.cancel_s_order, name='cancel_s_order'),
    path('viewcomplaintsearch', views.viewcomplaintsearch, name='viewcomplaintsearch'),
    path('viewcomplaint', views.viewcomplaint, name='viewcomplaint'),
    path('sendcomplaint', views.sendcomplaint, name='sendcomplaint'),
    path('sendrating', views.sendrating, name='sendrating'),
    path('viewoffers', views.viewoffers, name='viewoffers'),
    path('ordrprdctcodeand', views.ordrprdctcodeand, name='ordrprdctcodeand'),
    path('viewassigedwork', views.viewassigedwork, name='viewassigedwork'),
    path('view_notification', views.view_notification, name='view_notification'),
    path('updatestatus', views.updatestatus, name='updatestatus'),
    path('remove_item', views.remove_item, name='remove_item'),
    path('add_location', views.add_location, name='add_location'),
    path('check_un', views.check_un, name='check_un'),
    path('check_ph', views.check_ph, name='check_ph'),
    path('check_em', views.check_em, name='check_em'),
    path('sbydate', views.sbydate, name='sbydate'),
    path('view_bill', views.view_bill, name='view_bill'),
    path('view_bill_details', views.view_bill_details, name='view_bill_details'),



]
