from django.contrib import admin
from .models import EmployeRegister

# Register your models here.
class EmployeRegisterAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'address']
admin.site.register(EmployeRegister, EmployeRegisterAdmin)