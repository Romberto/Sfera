from django.contrib import admin
from .models import DriverModel, DriverAdminGroupModel

class DriverModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin_bool', 'login')

admin.site.register(DriverModel, DriverModelAdmin)
admin.site.register(DriverAdminGroupModel)
