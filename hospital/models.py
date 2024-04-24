from django.db import models

# Create your models here.


class tbldepartment(models.Model):
    department=models.CharField(max_length=10,null=True)
    status=models.CharField(max_length=10,null=True)

class tbldoctor(models.Model):
    name = models.CharField(max_length=10,null=True)
    email = models.EmailField(max_length=10,null=True)
    number = models.IntegerField(null=True)
    address = models.CharField(max_length=10,null=True)
    department = models.CharField(max_length=10,null=True)
    educationqualification = models.CharField(max_length=10,null=True)
    experience = models.CharField(max_length=10,null=True)
    drid = models.CharField(max_length=10,null=True)

class tblappointment(models.Model):
    firstname =models.CharField(max_length=10,null=True)
    lastname = models.CharField(max_length=10,null=True)
    email = models.CharField(max_length=10,null=True)
    phonenumber = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=10,null=True)
    age = models.CharField(max_length=10,null=True)
    purposeofvisit = models.CharField(max_length=10,null=True)

class tblreport(models.Model):
    nextappointment = models.CharField(max_length=10,null=True)
    appointmentdate = models.CharField(max_length=10,null=True)
    medicine = models.CharField(max_length=10,null=True)
    payment = models.CharField(max_length=10,null=True)

class tblcontact(models.Model):
    name = models.CharField(max_length=10,null=True)
    email = models.CharField(max_length=10,null=True)
    phone = models.IntegerField(max_length=10,null=True)
    subject = models.CharField(max_length=10,null=True)
    message = models.CharField(max_length=10,null=True)

class tblmedicine(models.Model):
    medicinename = models.CharField(max_length=10,null=True)
    medicinecode = models.CharField(max_length=10,null=True)
    medicineprice = models.CharField(max_length=10,null=True)
    amountofmedicine = models.CharField(max_length=10,null=True)
    expirydate = models.CharField(max_length=10,null=True)



