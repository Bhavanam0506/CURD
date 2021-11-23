from django.shortcuts import render,redirect
from django.views import View
from .models import car
from .home import CarForm


# Create your views here.
class Home(View):
    def get(self, request):
        car_info = car.objects.all()
        return render(request, 'home.html',{'cardata':car_info})

class add_car(View):
    def get(self,request):
        fm = CarForm()
        return render(request,'add-car.html', {'form':fm})

    def post(self, request):
        fm=CarForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request,'add-car.html', {'form':fm})


class del_car(View):
    def post(self,request):
        data = request.POST
        id = data.get('id')
        cardata=car.objects.get(id=id)
        cardata.delete()
        return redirect('/')

class upadate(View):
    def get(self,request,id):
        c= car.objects.get(id=id)
        fm= CarForm(instance=c)
        return render(request,'update-car.html',{'form':fm})
    def post(self,request, id):
        c= car.objects.get(id=id)
        fm = CarForm(request.POST, instance=c)
        if fm.is_valid():
            fm.save()
            return redirect('/')
class details(View):
    def get(self, request):
        car_detail = car.objects.all()
        return render(request, 'details.html',{'cardetails':car_detail})
        return redirect('/')

class list(View):
    def get(self, request):
        car_info = car.objects.all()
        return render(request, 'list.html',{'cardata':car_info})