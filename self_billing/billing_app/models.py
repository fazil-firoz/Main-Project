from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=100)
class staff(models.Model):
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    photo=models.FileField()

class security(models.Model):
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    photo=models.FileField()

class product(models.Model):
    productname=models.CharField(max_length=100)
    Description=models.TextField()
    Company=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)
    qr=models.CharField(max_length=100)
    image=models.FileField()
    stock=models.IntegerField()
    price=models.FloatField()
    Manufacturingdate=models.DateField()
    Expirydate=models.DateField()


class user(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField()
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)

class feedback(models.Model):
    USER=models.ForeignKey(user,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=100)
    date=models.DateField()
    rating=models.FloatField()

class offers(models.Model):
    PRODUCT=models.ForeignKey(product,on_delete=models.CASCADE)
    offers=models.IntegerField()
    details=models.CharField(max_length=100)
    fromdate=models.DateField()
    todate=models.DateField()
    type=models.CharField(max_length=100)

class order(models.Model):
    USER=models.ForeignKey(user,on_delete=models.CASCADE)
    amount=models.FloatField()
    date=models.DateField()
    status=models.CharField(max_length=100)
    ordertype=models.CharField(max_length=100)

class orderdetails(models.Model):
    ORDER=models.ForeignKey(order,on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField()

class orders(models.Model):
    STAFF = models.ForeignKey(staff,on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=100)
    price=models.IntegerField()
    username=models.CharField(max_length=156)
    phone=models.CharField(max_length=568)



class order_details (models.Model):
    PRODUCT = models.ForeignKey(product,on_delete=models.CASCADE)
    ORDER = models.ForeignKey(orders,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()



class deliveryboy(models.Model):
    name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.IntegerField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    lati = models.FloatField()
    longi = models.FloatField()
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)






class payment(models.Model):
    USER=models.ForeignKey(user,on_delete=models.CASCADE)
    amount=models.FloatField()
    date=models.DateField()
    status=models.CharField(max_length=100)
    ORDER=models.ForeignKey(order,on_delete=models.CASCADE)

class location(models.Model):
    DELIVERYBOY=models.ForeignKey(deliveryboy,on_delete=models.CASCADE)
    latitude=models.BigIntegerField()
    longitude=models.BigIntegerField()

# class complaint(models.Model):
#     USER=models.ForeignKey(user,on_delete=models.CASCADE)
#     complaint=models.CharField(max_length=100)
#     date=models.DateField()
#     reply=models.CharField(max_length=100)

class assign_order(models.Model):
    DELIVERYBOY=models.ForeignKey(deliveryboy,on_delete=models.CASCADE)
    order=models.ForeignKey(order,on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=100)





































































