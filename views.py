from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    districts = models.District.objects.all()
   

    context = {
        'districts': districts,
       
    }

    return render(request, 'home.html', context)
  
def view_district(request, pk):
    
    district = models.CholeraDatabase.objects.get(pk=pk)
    context = {
        'district' : district,
        
        
    }
    return render(request, 'view.html', context)