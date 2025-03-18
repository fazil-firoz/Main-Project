import json

from datetime import datetime
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from billing_app.models import *

import qrcode
import pyqrcode


from django.shortcuts import render
from qrcode.image.pil import PilImage


def logout(request):
    auth.logout(request)
    return render(request,'loginindex.html')

def home(request):
    return render(request, 'homeindex.html')
def login1(request):
    return render(request,'loginindex.html')

def logincode(request):
    print(request.POST)
    username=request.POST['textfield']
    password=request.POST['textfield2']
    try:
        ob=login.objects.get(username=username ,password=password)
        print(ob.type,"yyyyy")
        if ob.username!=username or ob.password!=password:
            return HttpResponse('''<Script>alert("Invalid user and password!");window.location="/"</Script>''')

        if ob.type=='admin':
            ob1=auth.authenticate(username="admin",password="adminadmin")
            if ob is not None:
                auth.login(request,ob1)
                request.session['lid']=ob.id

            return redirect("/adminhome")
        elif ob.type=='stockmanager':
            ob1 = auth.authenticate(username="admin", password="adminadmin")
            if ob is not None:
                auth.login(request, ob1)
                request.session['lid']=ob.id
            return redirect("/staffhome")
        else:
            return HttpResponse('''<Script>alert("Invalid user and password!1");window.location="/"</Script>''')
    except Exception as e:
        print(e,"dataa")
        return HttpResponse('''<Script>alert("Invalid user and password!2");window.location="/"</Script>''')
@login_required(login_url='/')

def adddelivery(request):
    return render(request, 'ADMIN/Add salesman.html')
@login_required(login_url='/')
def adddeliverycode(request):
    try:
        name=request.POST['textfield']
        gender=request.POST['radiobutton']
        place=request.POST['textfield3']
        post=request.POST['textfield4']
        pin=request.POST['textfield5']
        phone=request.POST['textfield6']
        email=request.POST['textfield7']
        uname=request.POST['textfield8']
        pswd=request.POST['textfield9']
        ob=login()
        ob.username=uname
        ob.password=pswd
        ob.type='deliveryboy'
        ob.save()
        on=deliveryboy()
        on.LOGIN=ob
        on.name=name
        on.Gender=gender
        on.lati='0'
        on.longi='0'
        on.place=place
        on.post=post
        on.pin=pin
        on.phone=phone
        on.email=email
        on.save()
        return redirect("/adminhome")
    except:
        return HttpResponse('''<Script>alert("Duplicate Entry...");window.location="/adminhome"</Script>''')






@login_required(login_url='/')
def add_stockmanager(request):
    return  render(request, 'ADMIN/ADD Stockmanager.html')
@login_required(login_url='/')
def add_stock_manager_post(request):

        fname=request.POST['textfield']
        lname=request.POST['textfield2']
        gender=request.POST['radiobutton']
        place=request.POST['textfield3']
        post=request.POST['textfield4']
        pin=request.POST['textfield5']
        phone=request.POST['textfield6']
        email=request.POST['textfield7']
        img=request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(img.name, img)
        uname=request.POST['textfield8']
        pswd=request.POST['textfield9']

        ob=login()
        ob.username=uname
        ob.password=pswd
        ob.type='stockmanager'
        ob.save()

        on=security()
        on.LOGIN=ob
        on.fname=fname
        on.lname=lname
        on.gender=gender
        on.place=place
        on.post=post
        on.pin=pin
        on.phone=phone
        on.email=email
        on.photo=fsave
        on.save()
        return HttpResponse("<script>alert('Stock manager  added');window.location='/adminhome'</script>")


@login_required(login_url='/')
def add_security(request):
    return  render(request, 'ADMIN/add security.html')
@login_required(login_url='/')
def add_security_post(request):

        fname=request.POST['textfield']
        lname=request.POST['textfield2']
        gender=request.POST['radiobutton']
        place=request.POST['textfield3']
        post=request.POST['textfield4']
        pin=request.POST['textfield5']
        phone=request.POST['textfield6']
        email=request.POST['textfield7']
        img=request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(img.name, img)
        uname=request.POST['textfield8']
        pswd=request.POST['textfield9']

        ob=login()
        ob.username=uname
        ob.password=pswd
        ob.type='security'
        ob.save()

        on=staff()
        on.LOGIN=ob
        on.fname=fname
        on.lname=lname
        on.gender=gender
        on.place=place
        on.post=post
        on.pin=pin
        on.phone=phone
        on.email=email
        on.photo=fsave
        on.save()
        return HttpResponse("<script>alert('Security added');window.location='/add_security'</script>")





@login_required(login_url='/')
def adminhome(request):
    return render(request,'ADMIN/index1.html')

@login_required(login_url='/')
def managesalesman(request):
    ob = deliveryboy.objects.all().order_by('-id')
    return render(request, 'ADMIN/MANAGE salesman.html', {'val':ob})


@login_required(login_url='/')
def managestaff(request):
    ob=staff.objects.all().order_by('-id')
    return render(request,'ADMIN/MANAGE STAFF.html',{'val':ob})

@login_required(login_url='/')
def search_staff(request):
    name = request.POST['textfield']
    ob = staff.objects.filter(fname__icontains=name)
    return render(request, 'ADMIN/MANAGE STAFF.html', {'val': ob})

@login_required(login_url='/')
def edit_staff(request,id):
    ob = staff.objects.get(id=id)
    request.session['SID']=id
    return render(request, 'ADMIN/edit_staff.html', {'val': ob})

@login_required(login_url='/')
def edit_stafff(request):
    if 'file' in request.FILES:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        gender = request.POST['radiobutton']
        place = request.POST['textfield3']
        post = request.POST['textfield4']
        pin = request.POST['textfield5']
        phone = request.POST['textfield6']
        email = request.POST['textfield7']
        img = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(img.name, img)


        on = staff.objects.get(id=request.session['SID'])
        on.fname = fname
        on.lname = lname
        on.gender = gender
        on.place = place
        on.post = post
        on.pin = pin
        on.phone = phone
        on.email = email
        on.photo = fsave
        on.save()
        return redirect("/managestaff")
    else:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        gender = request.POST['radiobutton']
        place = request.POST['textfield3']
        post = request.POST['textfield4']
        pin = request.POST['textfield5']
        phone = request.POST['textfield6']
        email = request.POST['textfield7']
        on = staff.objects.get(id=request.session['SID'])
        on.fname = fname
        on.lname = lname
        on.gender = gender
        on.place = place
        on.post = post
        on.pin = pin
        on.phone = phone
        on.email = email
        on.save()
        return redirect("/managestaff")


@login_required(login_url='/')
def edit_deliveryboy(request,id):
    ob = deliveryboy.objects.get(id=id)
    request.session['dID']=id
    return render(request, 'ADMIN/Edit Delivery.html', {'val': ob})

@login_required(login_url='/')
def edit_deliveryboycode(request):
        name = request.POST['textfield']
        gender = request.POST['radiobutton']
        place = request.POST['textfield3']
        post = request.POST['textfield4']
        pin = request.POST['textfield5']
        phone = request.POST['textfield6']
        email = request.POST['textfield7']
        on = deliveryboy.objects.get(id=request.session['dID'])
        on.name = name
        on.Gender = gender
        on.place = place
        on.post = post
        on.pin = pin
        on.phone = phone
        on.email = email
        on.save()
        return redirect("/managedelivery")

@login_required(login_url='/')
def delete_staff(request,id):
    ob = login.objects.get(id=id)
    ob.delete()
    return redirect("/managestaff")


@login_required(login_url='/')
def delete_deliveryboy(request,id):
    ob = login.objects.get(id=id)
    ob.delete()
    return redirect("/managedelivery")






#




@login_required(login_url='/')
def sendnotification(request):
    ob = notification.objects.all()
    return render(request,'ADMIN/Send Notification.html',{'val':ob})


@login_required(login_url='/')
def delete_noti(request,id):
    ob = notification.objects.get(id=id)
    ob.delete()
    return redirect("/sendnotification")






@login_required(login_url='/')
def viewcomplates(request):
    ob=complaint.objects.all()
    return render(request,'ADMIN/View complates.html',{'val':ob})


@login_required(login_url='/')

def viewproduts(request):
    ob = product.objects.filter(Expirydate__gte=datetime.today())

    return render(request,'ADMIN/View Products.html',{'val':ob})

@login_required(login_url='/')
def search_product(request):
    name = request.POST['textfield']
    cate = request.POST['textfield2']
    print(request.POST,"hhhhhhhhhhhhhhhh")
    if len(name)==0:
        ob = product.objects.filter(Category__icontains=cate)
    elif len(cate)==0:
        ob = product.objects.filter(productname__icontains=name)
    else:
        ob = product.objects.filter(Q(productname__icontains=name)|Q(Category__icontains=cate))
    return render(request, 'ADMIN/View Products.html', {'val': ob})


@login_required(login_url='/')
def viewpurchaseproduct(request):
    return render(request,'ADMIN/View  purchase Product.html')


@login_required(login_url='/')
def viewpurchase(request):
    ob= order.objects.all()

    return render(request,'ADMIN/View purchase.html',{'val':ob})


@login_required(login_url='/')
def sbydate(request):
    d=request.POST['d']
    s=request.POST['s']
    O=request.POST['O']
    if s=="ALL":
        ob= order.objects.filter(date=d,ordertype=O)

        return render(request,'ADMIN/View purchase.html',{'val':ob,"d":str(d)})
    else:

        ob = order.objects.filter(date=d,status=s,ordertype=O)

        return render(request, 'ADMIN/View purchase.html', {'val': ob, "d": str(d),"s":s})
def viewfeedback_admin(request):
    ob=feedback.objects.all()
    return render(request, 'ADMIN/View Feedback.html',{'val':ob})


@login_required(login_url='/')

def viewraiting(request):
    ob= feedback.objects.all()
    return render(request, 'ADMIN/View Raiting.html',{'val':ob})

@login_required(login_url='/')
def viewreply(request,id):
    request.session['Cid']=id
    return render(request, 'ADMIN/View reply.html')
@login_required(login_url='/')
def viewreply_post(request):
    reply = request.POST['textarea']
    ob=complaint.objects.get(id=request.session['Cid'])
    ob.reply=reply
    ob.save()
    return redirect("/viewcomplates")

@login_required(login_url='/')
def viewusers(request):
    ob = user.objects.all()
    return render(request, 'ADMIN/View Users.html',{'val':ob})

@login_required(login_url='/')
def addproduct(request):
    current_date = timezone.now()

    # Format the date as you desire
    formatted_date = current_date.strftime("%Y-%m-%d")
    return render(request, 'STAFF/Add product.html',{'d':formatted_date})
@login_required(login_url='/')
def addproductcode(request):
    productname=request.POST['textfield']
    Description=request.POST['textfield8']
    Company=request.POST['textfield7']
    Category=request.POST['textfield6']

    img = request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(img.name, img)
    Stock=request.POST['textfield2']
    price=request.POST['textfield3']
    Manufacturingdate=request.POST['textfield4']
    Expirydate=request.POST['textfield5']
    ob=product()
    ob.productname=productname
    ob.Description=Description
    ob.Company=Company
    ob.Category=Category
    ob.image=fsave
    ob.stock=Stock
    ob.price=price
    ob.Manufacturingdate=Manufacturingdate
    ob.Expirydate=Expirydate
    ob.qr = "media/qr/" + str(ob.id) + ".png"
    ob.save()
    # Data to encode in the QR code
    data = str(ob.id)
    ob.qr = "media/qr/" + str(ob.id) + ".png"
    ob.save()  # You can change this to your desired data

    # Generate a QR code instance
    ob1 = qrcode.QRCode(
        version=1,  # The QR code version (1-40), higher is a larger code.
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, H).
        box_size=10,  # The size of each box in the QR code.
        border=4,  # The border size around the QR code.
    )

    # Add data to the QR code
    ob1.add_data(data)
    ob1.make(fit=True)

    # Create a PIL (Python Imaging Library) image from the QR code data
    ob1 = ob1.make_image(fill_color="black", back_color="white")
    # Save the image to a file or display it
    ob1.save("media/qr/" + str(ob.id) + ".png")
    return redirect("/manageproduct")
@login_required(login_url='/')
def editproductcode(request):
    try:
        productname=request.POST['textfield']
        Description=request.POST['textfield8']
        Company=request.POST['textfield7']
        Category=request.POST['textfield6']

        img = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(img.name, img)
        Stock=request.POST['textfield2']
        price=request.POST['textfield3']
        Manufacturingdate=request.POST['textfield4']
        Expirydate=request.POST['textfield5']
        ob=product.objects.get(id=request.session['SID'])
        ob.productname=productname
        ob.Description=Description
        ob.Company=Company
        ob.Category=Category
        ob.image=fsave
        ob.stock=Stock
        ob.price=price
        ob.Manufacturingdate=Manufacturingdate
        ob.Expirydate=Expirydate
        ob.save()
        return redirect("/manageproduct")
    except:
        productname = request.POST['textfield']
        Description = request.POST['textfield8']
        Company = request.POST['textfield7']
        Category = request.POST['textfield6']



        Stock = request.POST['textfield2']
        price = request.POST['textfield3']
        Manufacturingdate = request.POST['textfield4']
        Expirydate = request.POST['textfield5']
        ob = product.objects.get(id=request.session['SID'])
        ob.productname = productname
        ob.Description = Description
        ob.Company = Company
        ob.Category = Category
        ob.stock = Stock
        ob.price = price
        ob.Manufacturingdate = Manufacturingdate
        ob.Expirydate = Expirydate
        ob.save()
        return  redirect("/manageproduct")

@login_required(login_url='/')
def editproductcodes(request):
    Stock=request.POST['textfield']
    ob=product.objects.get(id=request.session['ssid'])
    ob.stock=Stock
    ob.save()
    return redirect("/viewstock")

@login_required(login_url='/')
def assign(request,id):
    request.session['Oid']=id
    obb = assign_order.objects.filter(Q(status='not started')|Q(status='on the way')|Q(status='pending'))
    print(obb,"==========")
    lst=[]
    for i in obb:
        ob = deliveryboy.objects.filter(id=i.DELIVERYBOY.id)
        print(ob,"=========")
        for k in ob:
            lst.append(k.id)
    op=deliveryboy.objects.filter(~Q(id__in=lst))
    return render(request, 'STAFF/Assign.html',{'val':op})



@login_required(login_url='/')
def assignorder(request):
     dboy=request.POST['select']
     obb=assign_order.objects.filter(order__id=request.session['Oid'])
     if len(obb) == 0:
         ob=assign_order()
         ob.DELIVERYBOY=deliveryboy.objects.get(id=dboy)
         ob.order=order.objects.get(id=request.session['Oid'])
         ob.date=datetime.today()
         ob.status='pending'
         ob.save()
         return HttpResponse('''<Script>alert("Assigned !");window.location="/staffhome"</Script>''')
     else:
         return HttpResponse('''<Script>alert("Already assigned !");window.location="/staffhome"</Script>''')
@login_required(login_url='/')
def manageproduct(request):
    ob=product.objects.all().order_by('-id')
    return render(request, 'STAFF/Manage Product.html',{'val':ob})

@login_required(login_url='/')
def viewstock(request):
        ob=product.objects.filter(stock__lte=10)
        return render(request, 'STAFF/productviewstock.html',{'val':ob})


@login_required(login_url='/')
def editstock(request,id):
    request.session['ssid']=id
    ob=product.objects.get(id=id)
    return render(request, 'STAFF/updtstk.html',{'val':ob})

@login_required(login_url='/')
def deleteproduct(request,id):
    ob = product.objects.get(id=id)
    ob.delete()
    return redirect("/manageproduct")

@login_required(login_url='/')
def Editproduct(request,id):
    ob = product.objects.get(id=id)
    request.session['SID']=id
    return render(request, 'STAFF/edit product.html',{'val': ob,'mdate':str(ob.Manufacturingdate),'exdate':str(ob.Expirydate)})

@login_required(login_url='/')
def searchproduct(request):
    name=request.POST['textfield']
    ob = product.objects.filter(productname__icontains=name)
    return render(request, 'STAFF/Manage Product.html',{'val':ob})

@login_required(login_url='/')
def searchproducts(request):
    name=request.POST['textfield']
    ob = product.objects.filter(productname__icontains=name,stock__lte=10)
    return render(request, 'STAFF/productviewstock.html',{'val':ob})

@login_required(login_url='/')
def staffhome(request):
    return render(request, 'STAFF/staffindex.html')
@login_required(login_url='/')
def viewcomplatesstaff(request):
    ob = complaint.objects.all()
    return render(request, 'STAFF/View complates.html',{'val':ob})
@login_required(login_url='/')
def viewdeliverystatus(request):
    ob=assign_order.objects.all()
    return render(request, 'STAFF/View delivery status.html',{'val':ob})

@login_required(login_url='/')
def viewdproducts(request,id):
    ob = orderdetails.objects.filter(ORDER__id=id)
    return render(request,'STAFF/view delivery product.html',{'val':ob})
@login_required(login_url='/')
def viewfeedback(request):
    ob=feedback.objects.all()
    return render(request, 'STAFF/View Feedback.html',{'val':ob})

@login_required(login_url='/')
def viewnotification(request):
        return render(request, 'STAFF/View notification.html')

@login_required(login_url='/')
def viewonlineorder(request):
    ii=assign_order.objects.all()
    r=[]
    for i in ii:
        r.append(i.order.id)
    ob=order.objects.exclude(id__in=r)
    return render(request, 'STAFF/View Online order.html',{'val':ob})





@login_required(login_url='/')
def ordr_status(request):
    ob = orders.objects.filter(STAFF__LOGIN__id=request.session['lid'])
    return render(request, 'STAFF/order_status.html',{'val': ob})





@login_required(login_url='/')
def view_product(request,id):
    print(id,"++++++++++++++++++++++++++++++++++++++++++")
    ob=orderdetails.objects.filter(ORDER__id=id)
    print(ob,"=======")
    return render(request, 'STAFF/View product.html',{'val':ob})


"==========================ANDROID==============================="
def logincode1(request):
    print(request.POST)
    un = request.POST['uname']
    pwd = request.POST['pswd']
    print(un, pwd)
    try:
        ob = login.objects.get(username=un, password=pwd)

        if ob is None:
            data = {"task": "invalid"}
        else:
            print("in user function")
            data = {"task": "valid", "id": ob.id,"type":ob.type}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    except:
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)

def registration(request):
    try:
        Fname=request.POST['fname']
        image=request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(image.name, image)
        place= request.POST['place']
        post_office = request.POST['post']
        pin_code = request.POST['pin']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email_id = request.POST['email']
        uname = request.POST['username']
        passwd = request.POST['password']
        lob = login()
        lob.username = uname
        lob.password = passwd
        lob.type = 'user'
        lob.save()
        userob = user()
        userob.name = Fname
        userob.place = place
        userob.post = post_office
        userob.pin = pin_code
        userob.phone = phone
        userob.gender = gender
        userob.email = email_id
        userob.photo = fsave
        userob.LOGIN=lob
        userob.save()
        data = {"task": "valid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    except:

        data = {"task": "Duplicate"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)





"=====================order==========================="


def viewproduct(request):

    ob = product.objects.all()
    print(ob,"jjjjjjjjjj")
    data = []
    for i in ob:
        res = {'product': i.productname, 'image': i.image.url[7:], 'dis': i.Description,
                'pid': i.id}
        data.append(res)
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)


def vieworderstatus(request):
    lid=request.POST['lid']
    ob = assign_order.objects.filter(order__USER__LOGIN__id=lid)
    print(ob, "jjjjjjjjjj")
    data = []
    for i in ob:
        res = {'amnt':i.order.amount,'date':str(i.order.date),'status':i.order.status,'ordertype':i.order.ordertype,'orderid':i.id,'lati':i.DELIVERYBOY.lati,'longi':i.DELIVERYBOY.longi}
        data.append(res)
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)



def viewproductmore(request):
    pid=request.POST['pid']
    ob = product.objects.filter(id=pid)
    print(ob,"jjjjjjjjjj")
    data = []
    for i in ob:
        res = {'product': i.productname, 'image': i.image.url[7:], 'dis': i.Description,'qty':i.stock,'price':i.price,
                'pid': i.id,'cmp':i.Company,'ctgy':i.Category,'mdate':str(i.Manufacturingdate),'edate':str(i.Expirydate)}
        data.append(res)
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)


#

def ordrprdctcodeand(request):
    print(request.POST,"hhhhhhhhhhhh")
    qty=request.POST['qty']
    pid=request.POST['pid']
    lid=request.POST['lid']
    qq=product.objects.get(id=pid)
    tt = int(qq.price)* int(qty)
    stock = int(qq.stock)
    print(stock,qty,"jjjjjjjjjjjjjjjjjjjjjj")
    nstk = int(stock) - int(qty)
    if stock >= int(qty):
        up=product.objects.get(id=pid)
        up.stock=nstk
        up.save()
        q=order.objects.filter(USER=user.objects.get(LOGIN__id=lid),status='pending')
        if len(q)==0:
            qt=order()
            qt.date=datetime.today()
            qt.USER=user.objects.get(LOGIN=lid)
            qt.status='pending'
            qt.amount=tt
            qt.ordertype='online'
            qt.save()
            qty1=orderdetails()
            qty1.quantity=qty
            qty1.PRODUCT=product.objects.get(id=pid)
            qty1.ORDER=qt
            qty1.date = datetime.today()
            qty1.save()
            data = {"task": "valid"}
            r = json.dumps(data)
            print(r)
            return HttpResponse(r)
        else:
            total = int(q[0].amount) + int(tt)
            qt=order.objects.get(id=q[0].id)
            qt.amount=total
            qt.save()
            qty1=orderdetails.objects.filter(PRODUCT__id=pid,ORDER__id=q[0].id)
            if len(qty1)==0:
                qqt=orderdetails()
                qqt.ORDER=q[0]
                qqt.PRODUCT=product.objects.get(id=pid)
                qqt.quantity=qty
                qqt.save()
            else:
                qry1=orderdetails.objects.get(id=qty1[0].id)
                quty=int(qty1[0].quantity) + int(qty)
                qry1.quantity=quty
                qry1.save()
                data = {"task": "valid"}
                r = json.dumps(data)
                print(r)
                return HttpResponse(r)
    else:
        data = {"task": "out"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)





def ordrprdctcard(request):
    print(request.POST,"hhhhhhhhhhhh")
    qty=request.POST['qty']
    pid=request.POST['pid']
    lid=request.POST['lid']
    qq=product.objects.get(id=pid)
    tt = int(qq.price)* int(qty)
    stock = int(qq.stock)
    print(stock,qty,"jjjjjjjjjjjjjjjjjjjjjj")
    nstk = int(stock) - int(qty)
    if stock >= int(qty):
        up=product.objects.get(id=pid)
        up.stock=nstk
        up.save()
        q=order.objects.filter(USER=user.objects.get(LOGIN__id=lid),status='pending')
        if len(q)==0:
            qt=order()
            qt.date=datetime.today()
            qt.USER=user.objects.get(LOGIN=lid)
            qt.status='CART'
            qt.amount=tt
            qt.ordertype='online'
            qt.save()
            qty1=orderdetails()
            qty1.quantity=qty
            qty1.PRODUCT=product.objects.get(id=pid)
            qty1.ORDER=qt
            qty1.date = datetime.today()
            qty1.save()
            data = {"task": "valid"}
            r = json.dumps(data)
            print(r)
            return HttpResponse(r)
        else:
            total = int(q[0].amount) + int(tt)
            qt=order.objects.get(id=q[0].id)
            qt.amount=total
            qt.save()
            qty1=orderdetails.objects.filter(PRODUCT__id=pid,ORDER__id=q[0].id)
            if len(qty1)==0:
                qqt=orderdetails()
                qqt.ORDER=q[0]
                qqt.PRODUCT=product.objects.get(id=pid)
                qqt.quantity=qty
                qqt.save()
            else:
                qry1=orderdetails.objects.get(id=qty1[0].id)
                quty=int(qty1[0].quantity) + int(qty)
                qry1.quantity=quty
                qry1.save()
                data = {"task": "valid"}
                r = json.dumps(data)
                print(r)
                return HttpResponse(r)
    else:
        data = {"task": "out"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    data = {"task": "invalid"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)

def addtocart(request):
    print(request.POST, "hhhhhhhhhhhh")
    qty = request.POST['qty']
    pid = request.POST['pid']
    lid = request.POST['lid']
    qq = product.objects.get(id=pid)
    tt = int(qq.price) * int(qty)
    stock = int(qq.stock)
    print(stock, qty, "jjjjjjjjjjjjjjjjjjjjjj")
    nstk = int(stock) - int(qty)
    if stock >= int(qty):
        up = product.objects.get(id=pid)
        up.stock = nstk
        up.save()
        q = order.objects.filter(USER=user.objects.get(LOGIN__id=lid), status='pending')
        if len(q) == 0:
            qt = order()
            qt.date = datetime.today()
            qt.USER = user.objects.get(LOGIN=lid)
            qt.status = 'CART'
            qt.amount = tt
            qt.ordertype = 'online'
            qt.save()
            qty1 = orderdetails()
            qty1.quantity = qty
            qty1.PRODUCT = product.objects.get(id=pid)
            qty1.ORDER = qt
            qty1.date = datetime.today()
            qty1.save()
            data = {"task": "valid"}
            r = json.dumps(data)
            print(r)
            return HttpResponse(r)
        else:
            total = int(q[0].amount) + int(tt)
            qt = order.objects.get(id=q[0].id)
            qt.amount = total
            qt.save()
            qty1 = orderdetails.objects.filter(PRODUCT__id=pid, ORDER__id=q[0].id)
            if len(qty1) == 0:
                qqt = orderdetails()
                qqt.ORDER = q[0]
                qqt.PRODUCT = product.objects.get(id=pid)
                qqt.quantity = qty
                qqt.save()
            else:
                qry1 = orderdetails.objects.get(id=qty1[0].id)
                quty = int(qty1[0].quantity) + int(qty)
                qry1.quantity = quty
                qry1.save()
                data = {"task": "valid"}
                r = json.dumps(data)
                print(r)
                return HttpResponse(r)
    else:
        data = {"task": "out"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    data = {"task": "invalid"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)











@login_required(login_url='/')
def ordrprdct(request):

    my_objects = product.objects.all().order_by('-id')

    # Set the number of items per page
    items_per_page = 5

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)
    return render(request, 'STAFF/order products.html',{'my_objects':my_objects})






@login_required(login_url='/')
def srchordr_products(request):
    n = request.POST['textfield']
    my_objects = product.objects.filter(productname__icontains=n)

    # Set the number of items per page
    items_per_page = 5

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request, 'STAFF/order products.html', {'my_objects': my_objects})




# @login_required(login_url='/')
# def viewmycart(request):
#     try:
#         OB1=order.objects.get(USER__LOGINID__id=request.session['lid'],status='CART')
#         ob = order_details.objects.filter(ORDER__USER__LOGINID__id=request.session['lid'],ORDER__status='CART')
#         return render(request,'user/view my cart.html',{'val': ob,'total':OB1})
#     except:
#         ob = order_details.objects.filter(ORDER__USER__LOGINID__id=request.session['lid'],ORDER__status='CART')
#         return render(request,'user/view my cart.html',{'val': ob,'total':0})
#
#
#
# @login_required(login_url='/')
# def ordr_status(request):
#     ob = order.objects.filter(USER__LOGINID__id=request.session['lid'])
#     return render(request, 'user/order_status.html',{'val': ob})
#
#

@login_required(login_url='/')
def ordrdtls(request,id):
    request.session['pid']=id
    ob=product.objects.get(id=id)
    return render(request, 'STAFF/order details.html',{'val':ob})







@login_required(login_url='/')
def ordrprdctcode(request):
    btn=request.POST['Submit']
    if btn == 'ORDER NOW':
            print(request.session['pid'],"kiiiiiiiiiiiiiiiiiii")
            qty=request.POST['textfield3']
            qq=product.objects.get(id=request.session['pid'])
            tt = float(qq.price)* float(qty)
            stock = float(qq.stock)
            print(stock,qty,"jjjjjjjjjjjjjjjjjjjjjj")
            nstk = float(stock) - float(qty)
            if stock >= float(qty):
                up=product.objects.get(id=request.session['pid'])
                up.stock=nstk
                up.save()
                qt=orders()
                qt.date=datetime.today()
                qt.STAFF=staff.objects.get(LOGIN__id=request.session['lid'])
                qt.status='ORDER'
                qt.price=tt
                qt.username='pending'
                qt.phone='pending'
                qt.save()
                qty1=order_details()
                qty1.quantity=qty
                qty1.PRODUCT=product.objects.get(id=request.session['pid'])
                qty1.ORDER=qt
                qty1.date=datetime.today()
                qty1.save()
                return HttpResponse('''<script>alert('placed order successfuly');window.location='/staffhome'</script>''')
            else:
                return HttpResponse('''<script>alert('out of stock');window.location='/staffhome'</script>''')
    else:

        qty=request.POST['textfield3']
        qq=product.objects.get(id=request.session['pid'])
        tt = float(qq.price)* float(qty)
        stock = float(qq.stock)
        print(stock,qty,"jjjjjjjjjjjjjjjjjjjjjj")
        nstk = float(stock) - float(qty)
        if stock >= float(qty):
            up=product.objects.get(id=request.session['pid'])
            up.stock=nstk
            up.save()
            q=orders.objects.filter(STAFF=staff.objects.get(LOGIN__id=request.session['lid']),status='CART')
            if len(q)==0:
                qt=orders()
                qt.date=datetime.now()
                qt.STAFF=staff.objects.get(LOGIN__id=request.session['lid'])
                qt.status='CART'
                qt.price=tt
                qt.username = 'pending'
                qt.phone = 'pending'
                qt.save()
                qty1=order_details()
                qty1.quantity=qty
                qty1.PRODUCT=product.objects.get(id=request.session['pid'])
                qty1.ORDER=qt
                qty1.date = datetime.today()
                qty1.save()
                return HttpResponse('''<script>alert('ADD TO CART');window.location='/staffhome'</script>''')
            else:
                total = float(q[0].price) + float(tt)
                qt=orders.objects.get(id=q[0].id)
                qt.price=total
                qt.save()
                qty1=order_details.objects.filter(PRODUCT__id=request.session['pid'],ORDER__id=q[0].id)
                if len(qty1)==0:
                    qqt=order_details()
                    qqt.ORDER=q[0]
                    qqt.PRODUCT=product.objects.get(id=request.session['pid'])
                    qqt.quantity=qty
                    qqt.date=datetime.today()
                    qqt.save()
                else:
                    qry1=order_details.objects.get(id=qty1[0].id)
                    quty=float(qty1[0].quantity) + float(qty)
                    qry1.quantity=quty
                    qry1.date=datetime.today()
                    qry1.save()
                return HttpResponse('''<script>alert('ADD TO CART');window.location='/staffhome'</script>''')
        else:
            return HttpResponse('''<script>alert('OUT OF STOCK');window.location='/staffhome'</script>''')



@login_required(login_url='/')
def viewmycart(request):
    try:
        OB1=orders.objects.get(STAFF__LOGIN__id=request.session['lid'],status='CART')
        ob = order_details.objects.filter(ORDER__STAFF__LOGIN__id=request.session['lid'],ORDER__status='CART')
        return render(request,'STAFF/view my cart.html',{'val': ob,'total':OB1})
    except:
        ob = order_details.objects.filter(ORDER__STAFF__LOGIN__id=request.session['lid'],ORDER__status='CART')
        return render(request,'STAFF/view my cart.html',{'val': ob,'total':0})



@login_required(login_url='/')
def delete(request,id):
    obd = order_details.objects.get(id=id)
    request.session['oid'] = obd.ORDER.id
    obp = product.objects.get(id=obd.PRODUCT.id)
    obp.stock = float(obp.stock) + int(obd.quantity)
    obp.save()
    obd.delete()
    ob2 = order_details.objects.filter(ORDER__id=request.session['oid'])
    if len(ob2) == 0:
        ob1 = orders.objects.get(id=request.session['oid'])
        ob1.delete()
    return HttpResponse('''<script>alert("sended ");window.location='/ordrprdct#about'</script>''')
    # ob = order.objects.get(id=id)
    # ob.delete()
    # return HttpResponse('''<script>alert('send successfully....');window.location='/viewmycart#main'</script>''')


@login_required(login_url='/')
def orderfromcart(request,id):
    ob=orders.objects.get(id=id)
    ob.status='ORDER'
    ob.save()
    return render(request,'STAFF/view my cart.html')

@login_required(login_url='/')
def view_item_ordr_status(request,id):
    ob = order_details.objects.filter(ORDER__id=id)
    return render(request, 'STAFF/view_order_items.html', {'val': ob})


#============



def userGenerateBillamt(request):
    uid = request.POST['uid']
    # qry = "SELECT * FROM `bill` WHERE `S_id`=%s AND `Status`='finished'"
    res=order.objects.filter(USER__LOGIN__id=uid,status='CART')
    # val = uid
    # res = selectall2(qry, val)
    # ress=selectall2(qry,val)
    print("qwertyuiop",res)
    tot=0
    mdata = []
    for i in res:
        tot=float(tot)+float(i.amount)
        print("oioi",tot)
        data = {'date':str(i.date), 'amount': tot,'status':i.status,'id':i.id}
        mdata.append(data)
        print(mdata)
    r = json.dumps(mdata)
    return HttpResponse(r)



def userGenerateBill(request):
    # print(ob, "jjjjjjjjjj")
    lid=request.POST['lid']
    ob=orderdetails.objects.filter(ORDER__status='CART',ORDER__USER__LOGIN__id=lid)

    data = []
    for i in ob:
        ob1 = order.objects.filter(id=i.ORDER.id)
        res = {'date':str(i.ORDER.date), 'img': str(i.PRODUCT.image),'status':i.PRODUCT.productname,'qty':i.quantity,'id':i.id,'amt':ob1[0].amount,'oid':ob1[0].id}
        data.append(res)
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)














# def userGenerateBill(request):
#     uid = request.POST['uid']
#     # qry = "SELECT * FROM `bill` WHERE `S_id`=%s AND `Status`='finished'"
#     res = order.objects.filter(USER__LOGIN__id=uid, status='cart')
#     # val = uid
#     # res = selectall2(qry, val)
#     # ress=selectall2(qry,val)
#     print("qwertyuiop", res)
#     tot = 0
#     mdata = []
#     for i in res:
#         print(i.amount,"pppppppp")
#         tot = int(tot) + int(i['amount'])
#         data = {'date': i.date, 'amount': tot, 'status': i.status, 'id': i.id}
#         mdata.append(data)
#         print(mdata)
#     r = json.dumps(mdata)
#     return HttpResponse(r)




def userAddToCart1(request):
    print(request.POST)
    uid = request.POST['lid']
    print(uid)
    # qry = "SELECT `product`.`Name`,`product`.`Price`,`bill_details`.`Qty`,`bill`.`G_amount`,`bill_details`.`Id` FROM`product` JOIN`bill_details`ON`bill_details`.`P_id`=`product`.`P_id` JOIN`bill`ON`bill`.`B_id`=`bill_details`.`B_id` WHERE `bill`.`S_id`=%s AND  bill.Status='pending'"

    res = orderdetails.objects.filter(ORDER__USER__LOGIN__id=uid, ORDER__status='pending')

    mdata = []
    for i in res:

        data = {'Name': i.PRODUCT.productname, 'Price': i.ORDER.amount, 'Qty': i.quantity, 'id': i.id}
        mdata.append(data)
        print(mdata)
    r = json.dumps(mdata)
    return HttpResponse(r)

#
#
#
def select_product(request):
    pid = request.POST['pid']
    res = product.objects.filter(id=pid)

    mdata = []
    for i in res:
        data = {'Name': i.productname, 'Description': i.Description, 'Price': i.price, 'Image': i.image.url}
        mdata.append(data)
        print(mdata)
    r = json.dumps(mdata)
    return HttpResponse(r)

    #

#
#
#
# @app.route('/viewproduct', methods=['post'])
# def viewproduct():
#     pid=request.form['pid']
#     qry="SELECT * FROM `product` WHERE P_id='%s'"
#     val= (pid)
#     selectone(qry,val)
#     return jsonify({'task': "success"})
#
#
#
#
# @app.route('/generate_bill2', methods=['post'])
# def generate_bill2():
#     uid = request.form['lid']
#     qry = "SELECT `product`.`Name`,`bill_details`.`B_id`,`bill_details`.`Qty`,`product`.`Price` FROM `bill_details` JOIN `product` ON`product`.`P_id`=`bill_details`.`P_id` JOIN `bill` ON`bill`.`B_id`=`bill_details`.`B_id` WHERE `bill`.`S_id`=%s and `bill`.`Status`='pending'"
#     val = uid
#     res = selectall2(qry, val)
#     return jsonify(res)
#
#
#
#
#

#
# def generateBill3(request):
#     print("===================",request.POST)
#     qty = request.POST['qty']
#     lid = request.POST['lid']
#     pid = request.POST['pid']
#     p = request.POST['price']
#     tp = float(p) * int(qty)
#     # qry1 = "SELECT * FROM `bill` WHERE `S_id`=%s AND `Status`='pending'"
#     # res = selectone(qry1, lid)
#     res=order.objects.filter(USER__LOGIN__id=lid,status='pending')
#     print(res)
#     bid = 0
#     if len(res)==0:
#         obj=order()
#         obj.USER=user.objects.get(LOGIN__id=lid)
#         obj.amount=0
#         obj.ordertype='online'
#         obj.status='pending'
#         obj.date=datetime.now()
#         obj.save()
#
#     else:
#         bid = res
#         print("bid==========", bid)
#     res3=orderdetails.objects.filter(PRODUCT__id=pid,ORDER__USER__LOGIN__id=lid,ORDER__status='pending')
#     # qry3 = "SELECT `bill_details`.Id FROM `bill_details` JOIN `bill` ON `bill`.`B_id`= `bill_details`.`B_id` WHERE `bill`.`S_id`=%s AND `bill_details`.`P_id`=%s AND Status='pending'"
#     val3 = (lid, pid)
#     # res3 = selectone(qry3, val3)
#     print(res3, "================================")
#     if res3 is None:
#         obs=orderdetails()
#         obs.ORDER=order.objects.get(id=bid)
#         obs.PRODUCT=product.objects.get(id=pid)
#         obs.quantity=qty
#         obs.save()
#         # bdid = res3[5]
#         # qry2 = "INSERT INTO `bill_details` VALUES(NULL,%s,%s,%s)"
#         # val2 = (bid, pid, qty)
#         # iud(qry2, val2)
#     else:
#         bdid = res3
#         # qry4 = "UPDATE `bill_details` SET qty=qty+%s WHERE `Id`=%s"
#         # val4 = (qty, bdid)
#         # iud(qry4, val4)
#         obs=orderdetails.objects.get(id=bdid)
#         obs.quantity=int(obs.quantity)+int(qty)
#     # qry = "UPDATE `bill` SET `G_amount`=`G_amount`+%s WHERE `B_id`=%s"
#     # val = (tp, bid)
#     # iud(qry, val)
#     om=order.objects.get(id=bid)
#     om.amount=int(om.amount)+int(tp)
#     om.save()
#     data = {"status": "success"}
#     r = json.dumps(data)
#     print(r)
#     return HttpResponse(r)

# @app.route('/remove_item', methods=['post'])
# def remove_item():
#     print(request.form,"qwertyuio")
#     bid = request.form['bid']
#     qry1 = "DELETE FROM `bill` WHERE `B_id`=%s"
#     qry2 = "DELETE FROM `bill_details` WHERE `B_id`=%s"
#     iud(qry1, bid)
#     iud(qry2, bid)
#     return jsonify({'status': 'success'})


#
def finishBill(request):
    lid = request.POST['lid']
    # qry = "SELECT * FROM `bill` WHERE `S_id`=%s AND `Status`='pending'"
    # res = selectone(qry, lid)
    res=order.objects.get(USER__LOGIN__id=lid,status='pending')
    bid = 0
    print(res)
    if res is None:
        data = {"status": "fail"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    else:
        bid = res.id
        # qry = "UPDATE `bill` SET Status='finished' WHERE `B_id`=%s"
        # iud(qry, bid)
        obp=order.objects.get(id=bid)
        obp.status='finished'
        obp.save()

        data = {"status": "success"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)


# -----------------------------------------------------------------------



def orderscode(request):
    print(request.POST, "=================================")
    pro_id = request.POST['pid']
    qty = request.POST['quantity']
    lid = request.POST['lid']
    # off = request.POST['offer']
    print(pro_id, "PPPPPPPPPPPPPPPPPPPPPPP")
    print(qty, "qqqqqqqqqqqqqqqqqqqqqqq")
    print(lid, "lllllllllllllllllllllllll")

    ob = product.objects.get(id=pro_id)
    tt = float(ob.price) * int(qty)
    stock = ob.stock
    print(stock, "SSSSSSSSSSSSSSSSSSSSSSSSS")
    nstk = int(stock) - int(qty)
    print(nstk, "OOOOOOOOOOOOOOOOOOOO")
    if int(stock)>= int(qty):
        up = product.objects.get(id=pro_id)
        up.stock = nstk
        up.save()

        ob = order()
        ob.status = 'ORDER'
        ob.date = datetime.now()
        ob.USER = user.objects.get(LOGIN__id=lid)
        ob.amount = tt
        ob.ordertype='online'

        ob.save()

        obj = orderdetails()
        obj.ORDER = ob
        obj.PRODUCT=product.objects.get(id=pro_id)
        obj.quantity = qty
        # obj.quantity = 'ORDER'
        obj.save()
        id = ob.id
        data = {"task": "valid", "oid": id,"price":int(tt)}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    else:
        data = {"task": "out of stock"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)






def viewproductss(request):

    ob=product.objects.all()

    print(ob,"HHHHHHHHHHHHHHH")
    mdata = []
    for i in ob:
        data = {'productname': i.productname, 'image': str(i.image),'stock':i.stock,'price':i.price,'pid':i.id}
        mdata.append(data)
        print(mdata)
    r = json.dumps(mdata)
    return HttpResponse(r)



def viewproductsearch(request):
    asd=request.POST['shopname']
    ob=product.objects.filter(productname__istartswith=asd)

    print(ob,"HHHHHHHHHHHHHHH")
    mdata = []
    for i in ob:
        data = {'productname': i.productname, 'image': str(i.image),'stock':i.stock,'price':i.price,'pid':i.id}
        mdata.append(data)
        print(mdata)
    r = json.dumps(mdata)
    return HttpResponse(r)

def viewmyproductincard(request):
    lid=request.POST['lid']
    ob=orderdetails.objects.filter(ORDER__status='OFFCART',ORDER__USER__LOGIN=lid)

    print(ob,"HHHHHHHHHHHHHHH")
    mdata = []
    for i in ob:
        ob1 = order.objects.filter(id=i.ORDER.id)
        data = {'productname': i.PRODUCT.productname, 'image': str(i.PRODUCT.image),'stock':i.quantity,'price':i.ORDER.ordertype,'pid':i.id,'oid':ob1[0].id,'amt':ob1[0].amount}
        mdata.append(data)
        print(mdata)
    r = json.dumps(mdata)
    return HttpResponse(r)



def cancel_s_order(request):
    print(request.POST, "uuuuuuuuuuuuuuuu")
    qty=request.POST['qty']
    oid=request.POST['oid']
    obd = orderdetails.objects.get(id=oid)
    obp = product.objects.get(id=obd.PRODUCT.id)
    obp.stock = float(obp.stock) + int(qty)
    obp.save()
    id=obd.ORDER.id
    obd.delete()
    ob2 = orderdetails.objects.filter(ORDER__id=id)
    if len(ob2) == 0:
        ob1 = order.objects.get(id=id)
        ob1.delete()
    data = {"task": "valid"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)




def viewcomplaint(request):
    lid=request.POST['lid']
    ob=complaint.objects.filter(USER__LOGIN__id=lid)

    print(ob,"HHHHHHHHHHHHHHH")
    mdata = []
    for i in ob:
        data = {'complaint': i.complaint, 'date': str(i.date),'reply':i.reply,'id':i.id}
        mdata.append(data)
        print(mdata)
    r = json.dumps(mdata)
    return HttpResponse(r)


def viewcomplaintsearch(request):
    lid=request.POST['lid']
    date=request.POST['date']
    ob=complaint.objects.filter(date=date,USER__LOGIN__id=lid)

    print(ob,"HHHHHHHHHHHHHHH")
    mdata = []
    for i in ob:
        data = {'complaint': i.complaint, 'date': str(i.date),'reply':i.reply,'id':i.id}
        mdata.append(data)
        print(mdata)
    r = json.dumps(mdata)
    return HttpResponse(r)





#
#
# def add_to_cart(request):
#         print(request.POST,"=================================")
#         pro_id = request.POST['pro_id']
#         qty = request.POST['quantity']
#         lid = request.POST['lid']
#         print(pro_id, "PPPPPPPPPPPPPPPPPPPPPPP")
#         print(qty, "qqqqqqqqqqqqqqqqqqqqqqq")
#         print(lid, "lllllllllllllllllllllllll")
#
#         ob = product.objects.get(id=pro_id)
#         tt = float(ob.price) * int(qty)
#         print(tt,"price=====================tt========")
#         stock = ob.stock
#         print(stock, "SSSSSSSSSSSSSSSSSSSSSSSSS")
#         nstk = int(stock) - int(qty)
#         print(nstk, "OOOOOOOOOOOOOOOOOOOO")
#         if int(stock) >= int(qty):
#             up = product.objects.get(id=pro_id)
#             up.stock = nstk
#             up.save()
#
#
#
#
#             q = order.objects.filter(USER__LOGIN__id=lid, status='cart')
#             if len(q) == 0:
#
#                 obe = order()
#                 obe.amount = tt
#                 obe.status = 'cart'
#                 obe.ordertype='online'
#                 obe.date = datetime.now()
#
#                 obe.USER = user.objects.get(LOGIN__id=lid)
#                 obe.save()
#                 obe1 = orderdetails()
#                 obe1.quantity = qty
#                 obe1.ORDER = obe
#                 obe1.status = 'order'
#                 obe1.PRODUCT = up
#                 obe1.save()
#                 data = {"task": "valid"}
#                 r = json.dumps(data)
#                 print(r)
#                 return HttpResponse(r)
#
#
#
#             else:
#                 total = int(ob.price) + int(tt)
#                 print(total, "KKKKKKKKKKKKKKKK")
#
#                 obr = order.objects.get(id=q[0].id)
#                 print("hello good mrng")
#                 obr.amount= total
#                 obr.status = 'cart'
#                 obr.save()
#                 obr1 = orderdetails()
#                 obr1.quantity = qty
#                 obr1.ORDER = obr
#                 obr1.PRODUCT = up
#                 obr1.amount=total
#                 obr.save()
#                 obr1.save()
#                 data = {"task": "valid"}
#
#                 r = json.dumps(data)
#                 print(r)
#                 return HttpResponse(r)
#
#
#
#
#
#         else:
#             data = {"task": "out of stock"}
#             r = json.dumps(data)
#             print(r)
#             return HttpResponse(r)



def add_to_cart(request):
    print(request.POST, "hhhhhhhhhhhh")
    qty = request.POST['quantity']
    pid = request.POST['pro_id']
    lid = request.POST['lid']
    qq = product.objects.get(id=pid)
    tt = int(qq.price) * int(qty)
    stock = int(qq.stock)
    print(stock, qty, "jjjjjjjjjjjjjjjjjjjjjj")
    nstk = int(stock) - int(qty)
    if stock >= int(qty):
        up = product.objects.get(id=pid)
        up.stock = nstk
        up.save()
        q = order.objects.filter(USER=user.objects.get(LOGIN__id=lid), status='OFFCART')
        if len(q) == 0:
            qt = order()
            qt.date = datetime.today()
            qt.USER = user.objects.get(LOGIN=lid)
            qt.status = 'OFFCART'
            qt.amount = tt
            qt.ordertype = 'online'
            qt.save()
            qty1 = orderdetails()
            qty1.quantity = qty
            qty1.PRODUCT = product.objects.get(id=pid)
            qty1.ORDER = qt
            qty1.date = datetime.today()
            qty1.save()
            data = {"task": "valid"}
            r = json.dumps(data)
            print(r)
            return HttpResponse(r)
        else:
            total = int(q[0].amount) + int(tt)
            qt = order.objects.get(id=q[0].id)
            qt.amount = total
            qt.save()
            qty1 = orderdetails.objects.filter(PRODUCT__id=pid, ORDER__id=q[0].id)
            if len(qty1) == 0:
                qqt = orderdetails()
                qqt.ORDER = q[0]
                qqt.PRODUCT = product.objects.get(id=pid)
                qqt.quantity = qty
                qqt.save()
            else:
                qry1 = orderdetails.objects.get(id=qty1[0].id)
                quty = int(qty1[0].quantity) + int(qty)
                qry1.quantity = quty
                qry1.save()
                data = {"task": "valid"}
                r = json.dumps(data)
                print(r)
                return HttpResponse(r)
    else:
        data = {"task": "out"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    data = {"task": "invalid"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)



def paymentfinish(request):

    oid=request.POST['bid']
    amount=request.POST['amt']
    lid=request.POST['lid']
    ob = payment()
    ob.ORDER=order.objects.get(id=oid)
    ob.USER=user.objects.get(LOGIN__id=lid)
    ob.status='PAID'
    ob.amount=amount
    ob.date=datetime.now()
    ob.save()
    obj=order.objects.get(id=oid)
    obj.status='PAID'
    obj.save()
    data = {"task": "success"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)



def sendcomplaint(request):
    comp=request.POST['complaint']
    lid=request.POST['lid']
    lob = complaint()
    lob. complaint= comp
    lob. USER= user.objects.get(LOGIN__id=lid)
    lob.reply = 'pending'
    lob.date = datetime.today()
    lob.save()

    data = {"task": "valid"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)

def sendrating(request):
    feed=request.POST['feedback']
    rate=request.POST['rating']
    lid=request.POST['lid']
    lob =feedback()
    lob. feedback= feed
    lob. rating= rate
    lob. USER= user.objects.get(LOGIN__id=lid)
    lob.date = datetime.today()
    lob.save()

    data = {"task": "valid"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)





def updatestatus(request):
    feed=request.POST['status']
    rate=request.POST['aid']

    lob =assign_order.objects.get(id=rate)
    lob. status= feed

    lob.save()

    data = {"task": "valid"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)

def viewoffers(request):

    ob = offers.objects.all()
    print(ob,"jjjjjjjjjj")
    data = []
    for i in ob:
        res = {'product': i.PRODUCT.productname, 'image': i.PRODUCT.image.url[7:], 'offer':i.offers,'details':i.details,'fdate':str(i.fromdate),'type':i.type,'tdate':str(i.todate),
                'id': i.id}

        data.append(res)
        print(data)
    r = json.dumps(data)
    return HttpResponse(r)




def generateBill3(request):
    print(request.POST, "hhhhhhhhhhhh")
    qty = request.POST['qty']
    pid = request.POST['pid']
    lid = request.POST['lid']
    qq = product.objects.get(id=pid)
    tt = int(qq.price) * int(qty)
    stock = int(qq.stock)
    print(stock, qty, "jjjjjjjjjjjjjjjjjjjjjj")
    nstk = int(stock) - int(qty)
    if stock >= int(qty):
        up = product.objects.get(id=pid)
        up.stock = nstk
        up.save()
        q = order.objects.filter(USER=user.objects.get(LOGIN__id=lid), status='CART')
        if len(q) == 0:
            qt = order()
            qt.date = datetime.today()
            qt.USER = user.objects.get(LOGIN=lid)
            qt.status = 'CART'
            qt.amount = tt
            qt.ordertype = 'offline'
            qt.save()
            qty1 = orderdetails()
            qty1.quantity = qty
            qty1.PRODUCT = product.objects.get(id=pid)
            qty1.ORDER = qt
            qty1.date = datetime.today()
            qty1.save()
            data = {"task": "valid"}
            r = json.dumps(data)
            print(r)
            return HttpResponse(r)
        else:
            total = int(q[0].amount) + int(tt)
            qt = order.objects.get(id=q[0].id)
            qt.amount = total
            qt.save()
            qty1 = orderdetails.objects.filter(PRODUCT__id=pid, ORDER__id=q[0].id)
            if len(qty1) == 0:
                qqt = orderdetails()
                qqt.ORDER = q[0]
                qqt.PRODUCT = product.objects.get(id=pid)
                qqt.quantity = qty
                qqt.save()
            else:
                qry1 = orderdetails.objects.get(id=qty1[0].id)
                quty = int(qty1[0].quantity) + int(qty)
                qry1.quantity = quty
                qry1.save()
                data = {"task": "valid"}
                r = json.dumps(data)
                print(r)
                return HttpResponse(r)
    else:
        data = {"task": "out"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    data = {"task": "invalid"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)






def viewassigedwork(request):
    # print(ob, "jjjjjjjjjj")
    lid=request.POST['lid']
    ob=assign_order.objects.filter(DELIVERYBOY__LOGIN__id=lid)

    data = []
    for i in ob:
        res = {'date':str(i.date), 'name': i.order.USER.name,'phone':i.order.USER.phone,'id':i.id,'place':i.order.USER.place,'post':i.order.USER.place}
        data.append(res)
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)



#
# def view_notification(request):
#
#     ob=notification.objects.all()
#     data = []
#     for i in ob:
#         res = {'date':str(i.date), 'notification': i.notification}
#         data.append(res)
#     r = json.dumps(data)
#     print(r)
#     return HttpResponse(r)



def view_notification(request):
    ob=notification.objects.all()

    data = []
    for i in ob:
        res = {'date': str(i.date), 'notification': i.notification}
        data.append(res)
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)






def remove_item(request):
    print(request.POST, "uuuuuuuuuuuuuuuu")
    qty=request.POST['qty']
    oid=request.POST['oid']
    obd = orderdetails.objects.get(id=oid)
    obp = product.objects.get(id=obd.PRODUCT.id)
    obp.stock = float(obp.stock) + int(qty)
    obp.save()
    id=obd.ORDER.id
    obd.delete()
    ob2 = orderdetails.objects.filter(ORDER__id=id)
    if len(ob2) == 0:
        ob1 = order.objects.get(id=id)
        ob1.delete()
    data = {"task": "success"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)



def add_location(request):
    lati=request.POST['latitude']
    longi=request.POST['longitude']
    lid=request.POST['lid']
    lob= deliveryboy.objects.get(LOGIN__id=lid)
    lob.lati = lati
    lob.longi = longi
    lob.save()
    data = {"task": "valid"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)



def check_un(request):
    un=request.GET['username']
    ob = login.objects.filter(username=un)
    r={"key":False}
    if len(ob)>0:
        r['key']=True
    return JsonResponse(r)

def check_ph(request):
    ph=request.GET['phno']

    ob = user.objects.filter(phone=ph)
    r={"key":False}
    if len(ob)>0:
        r['key']=True
    else:
        os = deliveryboy.objects.filter(phone=ph)
        r = {"key": False}
        if len(os) > 0:
            r['key'] = True
        else:
            os = staff.objects.filter(phone=ph)
            r = {"key": False}
            if len(os) > 0:
                r['key'] = True

    return JsonResponse(r)

def check_em(request):
    em=request.GET['em'].replace('%40','@')
    print(em)

    ob = user.objects.filter(email=em)
    r={"key":False}
    if len(ob)>0:
        r['key']=True
    else:
        os = deliveryboy.objects.filter(email=em)

        if len(os) > 0:
            r['key'] = True
        else:
            os = staff.objects.filter(email=em)
            r = {"key": False}
            if len(os) > 0:
                r['key'] = True
    print(r)
    return JsonResponse(r)




def view_bill(request):
    lid=request.POST['lid']
    print(lid, "lid")
    ob=order.objects.filter(USER__LOGIN__id=lid)

    data = []
    for i in ob:
        res = {'date': str(i.date), 'amount': i.amount,'status':i.status,'type':i.ordertype,'id':i.id}
        data.append(res)
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)


def view_bill_details(request):
    lid=request.POST['oid']
    print(lid)
    ob=orderdetails.objects.filter(ORDER__id=lid)
    obb = order.objects.get(id=lid)
    data = []
    for i in ob:
        res = {'product': i.PRODUCT.productname,'qty':i.quantity,'price':int(i.quantity)*int(i.PRODUCT.price),"total":obb.amount,'id':obb.id}
        data.append(res)
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)

