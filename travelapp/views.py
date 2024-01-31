from django.shortcuts import render
from . models import place,teammates
# from django.http import HttpResponse



# Create your views here.
def demo(request):
    obj = place.objects.all()
    obj2 = teammates.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})

# def demo2(request):
#     obj2 = teammates.objects.all()
#     return render(request,"index.html",{'result2':obj2})