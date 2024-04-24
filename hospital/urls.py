from django.urls import path
from.import views

urlpatterns = [
    path("",views.index),
    path("adminlogin/",views.adminloging),
    path("checklogin/", views.checklogin),
    path("homepage/", views.homepage),
    path("adddoctor/",views.adddoctor),
    path("adddepartment/",views.adddepartment),
    path("savedepartment/",views.savedepartment),
    path("viewdepartment/",views.viewdepartment),
    path("editdepartment/<id>", views.editdepartment),
    path("updatedepartment/<id>", views.updatedepartment),
    path("deletedepartment/<id>", views.deletedepartment),
    path("savedoctor/", views.savedoctor),
    path("viewdoctor/", views.viewdoctor),
    path("editdoctor/<id>", views.editdoctor),
    path("updatedoctor/<id>", views.updatedoctor),
    path("deletedoctor/<id>", views.deletedoctor),
    path("appointmentform/", views.appointmentform),
    path("saveappointment/", views.saveappointment),
    path("contact/", views.contact),
    path("blogsingle/", views.blogsingle),
    path("error/", views.error),
    path("booking/",views.booking),
    path("reportappointment/<id>",views.reportappointment),
    path("savereport/", views.savereport),
    path("savecontact/", views.savecontact),
    path("viewcontact/", views.viewcontact),
    path("doctor/", views.doctor),
    path("addmedicine/",views.addmedicine),
    path("savemedicine/",views.savemedicine),
    path("viewmedicine/",views.viewmedicine),
    path("editmedicine/<id>",views.editmedicine),
    path("updatemedicine/<id>",views.updatemedicine),
    path("deletemedicine/<id>",views.deletemedicine),
    path("medicine/",views.medicine),
    path("medicine_single/<id>",views.medicine_single),
    path("paymenthandler/",views.paymenthandler),
    path("payment_success/",views.payment_success)


]