import razorpay
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .models import *


# Create your views here.
def index(request):
    return render(request,"index.html")

def blogsingle(request):
    return render(request,"blogsingle.html")

def contact(request):
    return render(request,"contact.html")

def error(request):
    return render(request,"error.html")


def adminloging(request):
    return render(request,"adminloging.html")



def checklogin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/homepage/")
        else:
            return redirect("/adminlogin/")

def homepage(request):
    return render(request,"homepage.html")

def adddoctor(request):
    return render(request,"adddoctor.html")

def adddepartment(request):
    return render (request,"adddepartment.html")

def savedepartment(request):
    a=tbldepartment()
    a.department = request.POST.get("department")
    a.status = request.POST.get("status")
    a.save()
    return redirect("/adddepartment/")

def viewdepartment(request):
    a = tbldepartment.objects.all
    return render(request, "viewdepartment.html", {'a': a})

def editdepartment(request,id):
    b=tbldepartment.objects.get(id=id)
    return render(request,"editdepartment.html",{'b': b})

def updatedepartment(request,id):
    c=tbldepartment.objects.get(id=id)
    c.department = request.POST.get("department")
    c.status = request.POST.get("status")
    c.save()
    return redirect("/viewdepartment/")

def deletedepartment(request,id):
    d=tbldepartment.objects.get(id=id)
    d.delete()
    return redirect("/viewdepartment/")

def savedoctor(request):
    a=tbldoctor()
    a.name = request.POST.get("name")
    a.email = request.POST.get("email")
    a.number = request.POST.get("number")
    a.address = request.POST.get("address")
    a.department = request.POST.get("department")
    a.educationqualification = request.POST.get("education qualification")
    a.experience = request.POST.get("experience")
    a.drid = request.POST.get("dr id")
    a.save()
    return redirect("/adddoctor/")

def viewdoctor(request):
    a = tbldoctor.objects.all
    return render(request, "viewdoctor.html", {'a': a})

def editdoctor(request,id):
    b=tbldoctor.objects.get(id=id)
    return render(request,"editdoctor.html",{'b': b})


def updatedoctor(request,id):
    c=tbldoctor.objects.get(id=id)
    c.name = request.POST.get("name")
    c.email = request.POST.get("email")
    c.number = request.POST.get("number")
    c.address = request.POST.get("address")
    c.department = request.POST.get("department")
    c.educationqualification = request.POST.get("education qualification")
    c.expereince = request.POST.get('experience')
    c.drid = request.POST.get("dr id")
    c.save()
    return redirect("/viewdoctor/")

def deletedoctor(request,id):
    d=tbldoctor.objects.get(id=id)
    d.delete()
    return redirect("/viewdoctor/")

def appointmentform(request):
    return render(request,"appointmentform.html")


def saveappointment(request):
    a=tblappointment()
    a.firstname = request.POST.get("firstname")
    a.lastname = request.POST.get("lastname")
    a.email = request.POST.get("email")
    a.phonenumber = request.POST.get("phonenumber")
    a.address = request.POST.get("address")
    a.age = request.POST.get("age")
    a.purposeofvisit = request.POST.get("purposeofvisit")
    a.save()
    return redirect("/")


def booking(request):
    a = tblappointment.objects.all()
    return render(request, "booking.html", {'a': a})



def reportappointment(request,id):
    b=tblappointment.objects.get(id=id)
    return render(request,"reportappointment.html",{'b': b})


def savereport (request):
    a=tblreport()
    a.nextappointment = request.POST.get("nextappointment")
    a.appointmentdate = request.POST.get("appointmentdate")
    a.medicine = request.POST.get("medicine")
    a.payment = request.POST.get("payment")
    a.save()
    return redirect("/booking/")

def savecontact (request):
    a=tblcontact()
    a.name = request.POST.get("name")
    a.email = request.POST.get("email")
    a.phone = request.POST.get("phone")
    a.subject = request.POST.get("subject")
    a.message = request.POST.get("message")
    a.save()
    return redirect("/")

def viewcontact(request):
    a = tblcontact.objects.all()
    return render(request,"viewcontact.html",{'a':a})


def doctor(request):
    a = tbldoctor.objects.all()

    return render(request,"doctor.html",{'a':a})

def addmedicine(request):
    return render (request,"addmedicine.html")

def savemedicine(request):
    a=tblmedicine()
    a.medicinename = request.POST.get("medicinename")
    a.medicinecode = request.POST.get("medicinecode")
    a.medicineprice = request.POST.get("medicineprice")
    a.amountofmedicine = request.POST.get("amountofmedicine")
    a.expirydate = request.POST.get("expirydate")
    a.save()
    return redirect("/addmedicine")

def viewmedicine(request):
    a = tblmedicine.objects.all
    return render(request, "viewmedicine.html", {'a': a})

def editmedicine(request,id):
    b=tblmedicine.objects.get(id=id)
    return render(request,"editmedicine.html",{'b': b})


def updatemedicine(request,id):
    c=tblmedicine.objects.get(id=id)
    c.medicinename = request.POST.get("medicinename")
    c.medicinecode = request.POST.get("medicinecode")
    c.medicineprice = request.POST.get("medicineprice")
    c.amountofmedicine = request.POST.get("amountofmedicine")
    c.expirydate = request.POST.get("expirydate")
    c.save()
    return redirect("/viewmedicine/")

def deletemedicine(request,id):
    d=tblmedicine.objects.get(id=id)
    d.delete()
    return redirect("/viewmedicine/")


razorpay_client = razorpay.Client(auth=('rzp_test_sEU3RKHFgCx23a','YYzkNd8erSik7IK1tnPZL5nY'))
def medicine(request):
    a=tblmedicine.objects.all()
    return render(request, "medicine.html",{'a':a})

def medicine_single(request,id):
    f=tblmedicine.objects.get(id=id)
    currency = 'INR'
    amount = int(f.medicineprice) * 100
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler'

    context = {}
    context['razorpay_order_id'] = razorpay_order_id

    context['razorpay_merchant_key'] = 'rzp_test_sEU3RKHFgCx23a'
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    context['price']=f.medicineprice
    context['data']=f
    return render(request,"medicine_single.html",context)

def paymenthandler(request):
    razorpay_order_id = request.POST.get('razorpay_order_id')

    payment_id = request.POST.get('payment_id', '')
    print('paymentid:', str(payment_id))

    signature = request.POST.get('razorpay_signature', '')

    params_dict = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_payment_id': payment_id,
        'razorpay_signature': signature
    }

    # verify the payment signature.
    price = request.POST.get('price', '')
    print("res:")
    amount = int(price) * 100  # Rs. 200
    razorpay_client.payment.capture(payment_id, amount)
    return redirect("/payment_success/")

def payment_success(request):
    return render(request,"payment_success.html")
