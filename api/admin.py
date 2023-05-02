from django.contrib import admin
from .models import Company,Employees
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)

class EmployeesAdmin(admin.ModelAdmin):
    list_display=('name','emails','company')

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employees,EmployeesAdmin)
