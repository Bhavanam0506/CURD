from django.contrib import admin
from .models import car
# Register your models here.
@admin.register(car)
class carAdmin(admin.ModelAdmin):
    list_display = ['id','name','type','avg_s']