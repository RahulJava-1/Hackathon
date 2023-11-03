from django.shortcuts import render,redirect,reverse
from . models import Register, AdminLogin, DoctorLogin
from adminzone.models import AddDoc
import random
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def registration(request):
    return render(request,'registration.html')

def patientLogin(request):
    return render(request,'patientLogin.html')

def cardio(request):
    return render(request,'cardio.html')

def gastro(request):
    return render(request,'gastro.html')

def neuro(request):
    return render(request,'neuro.html')

def ortho(request):
    return render(request,'ortho.html')

def doctorlogin(request):
    return render(request,'doctorlogin.html')

def adminlogin(request):
    return render(request,'adminlogin.html')

def regSignup(request):
    fname=request.POST['fname'] 
    lname=request.POST['lname'] 
    gender=request.POST['gender']
    contact=request.POST['contact']
    age=request.POST['age']
    height=request.POST['height']
    aadhar=request.POST['aadhar']
    weight=request.POST['weight']
    address=request.POST['address']
    uniqueID=random.randint(0,999999)
    email=request.POST['email']
    try:
        msg = 'Message:'
        msg = msg+'This Email Id is already exists'
        Register.objects.get(email = email)
        return render(request,'registration.html',{'msg':msg})
    except Register.DoesNotExist:
        password=request.POST['password']
        msg ='Message: '
        if len(password)<8:
            msg=msg+'Password must be atleast 8 digit'
            return render(request,'registration.html',{'msg':msg})
        else:
            r=Register(fname=fname,lname=lname,gender=gender,contact=contact,email=email,age=age,height=height,aadhar=aadhar,weight=weight,password=password,address=address,uniqueID=uniqueID)
            r.save()
            return redirect(reverse('unique'),{'uniqueID':uniqueID})

def unique(request):
    un = Register.objects.all()
    un=random.randint(0,999999)
    return HttpResponse(un,content_type='text/plain')
    # return render(request,'unique.html',{'un':un})

def vPatient(request):
    emailid = request.POST['emailid']
    password = request.POST['password']
    msg=''
    try:
        cust = Register.objects.get(email=emailid, password=password)
        if cust is not None:
            request.session['emailid'] = emailid
            return redirect(reverse('patient_zone:phome'))
            
    except ObjectDoesNotExist:
        msg = msg+"Invalid Email ID or Password"
    return render(request,'patientLogin.html',{'msg':msg})

def vAdmin(request):
    adminid=request.POST['adminid']
    password=request.POST['password']
    msg=''
    try:
        admin=AdminLogin.objects.get(adminid=adminid,password=password)
        if admin is not None:
            request.session['adminid'] = adminid
            return redirect(reverse('adminzone:adminhome'))
    except ObjectDoesNotExist:
        msg=msg+'Invalid User'
    return render(request,'adminlogin.html',{'msg':msg})

def vDoctor(request):
    docId = request.POST['docId']
    password = request.POST['password']
    msg=''
    try:
        doc = AddDoc.objects.get(docId=docId,password=password)
        if doc is not None:
            request.session['docId']=docId
            return redirect(reverse('doctor_zone:docHome'))
    except ObjectDoesNotExist:
        msg=msg+'Invalid userId or Password'
    return render(request,'doctorlogin.html',{'msg':msg})