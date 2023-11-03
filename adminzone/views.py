from django.shortcuts import render,redirect,reverse
from genzone.models import Register
from adminzone.models import AddDoc
# Create your views here.

def adminhome(request):
    try:
        if request.session['adminid']:
            return render(request,'adminhome.html')
    except KeyError:
        return render(request,'adminlogin.html')
    
def patient(request):
    try:
        if request.session['adminid']:
            user = Register.objects.all()
            return render(request,'patient.html',{'user':user})
    except KeyError:
        return render(request,'adminlogin.html')
    
def doctor(request):
    try:
        if request.session['adminid']:
            return render(request,'doctor.html')
    except KeyError:
        return render(request,'adminlogin.html')

def docPage(request):
    try:
        if request.session['adminid']:
            doc = AddDoc.objects.all()
            return render(request,'docPage.html',{'doc':doc})
    except KeyError:
        return render(request, 'adminlogin.html')

def addDoc(request):
            name = request.POST['name']
            contact = request.POST['contact']
            department = request.POST['department']
            docId = request.POST['docId']
            password = request.POST['password']
            ad = AddDoc(name=name,contact=contact,department=department,docId=docId,password=password)
            ad.save()
            return redirect('adminzone:doctor')

def deleteDoc(request,id):
    d = AddDoc.objects.get(docId=id)
    d.delete()
    return redirect('adminzone:docPage')

def deletePat(request,eid):
    u = Register.objects.get(email=eid)
    u.delete()
    return redirect('adminzone:patient')

def logout(request):
    try:
        if request.session['adminid']:
            request.session['adminid']=None
            return render(request,'adminlogin.html')
    except KeyError:
        return render(request,'adminlogin.html')