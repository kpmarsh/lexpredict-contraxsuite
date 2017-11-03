from django.contrib import admin

# Project imports
from apps.employee.models import (Employee, Employer,Noncompete_Provision)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'annual_salary')
    search_fields = ('name',)

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('name',)

class NoncompeteProvisionAdmin(admin.ModelAdmin):
    list_display =('text_unit', 'similarity')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(Noncompete_Provision, NoncompeteProvisionAdmin)
