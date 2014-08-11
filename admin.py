from django.contrib import admin
from models import  *

# Register your models here.
class departmentAdmin(admin.ModelAdmin):
    list_display = ('id','no','name','parent')
    search_fields = ('name','no')

admin.site.register(department, departmentAdmin)

class staffAdmin(admin.ModelAdmin):
    list_display = ('sid','department','supervisor','name','gender','current_year_balance','last_years_balance','pending_deduction')
    search_fields = ('name','department__name')

admin.site.register(staff, staffAdmin)

class supervisor_listAdmin(admin.ModelAdmin):
    list_display = ('supervisor','active')
    search_fields = ('supervisor__name',)

admin.site.register(supervisor_list, supervisor_listAdmin)

