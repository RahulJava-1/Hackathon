from django.shortcuts import render
from genzone.models import Register

# Create your views here.
def phome(request):
    try:
        if request.session['emailid']:
            return render(request,'phome.html')
    except KeyError:
        return render(request,'patientLogin.html')

def logout(request):
    try:
        if request.session['emailid']:
            request.session['emailid']=None
            return render(request,'patientLogin.html')
    except KeyError:
        return render(request,'patientLogin.html')