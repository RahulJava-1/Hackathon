from django.shortcuts import render

# Create your views here.
def docHome(request):
    return render(request,'docHome.html')

def logout(request):
    try:
        if request.session['docId']:
            request.session['docId']=None
            return render(request,'doctorlogin.html')
    except KeyError:
        return render(request,'doctorlogin.html')
