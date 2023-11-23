from django.contrib import admin
from .models import Issue
# Register your models here.

class IssueAdmin(admin.ModelAdmin):
    pass

admin.site.register(Issue,IssueAdmin)
