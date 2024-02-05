from django.contrib import admin
from .models import Complaint
# Register your models here.

class ComplaintAdmin(admin.ModelAdmin):
    list_display=("user","title","category","description","images","date_created","status")
    



admin.site.register(Complaint, ComplaintAdmin)
