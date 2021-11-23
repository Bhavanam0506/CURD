from django.urls import path
from .views import Home, add_car,del_car, upadate,details,list

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add-car/',add_car.as_view(),name='add-car'),
    path('del_car/',del_car.as_view(), name='del_car'),
    path('update-car/<int:id>/',upadate.as_view(),name='update-car'),
    path('details',details.as_view(),name='details'),
    path('list',list.as_view(),name='list')
]