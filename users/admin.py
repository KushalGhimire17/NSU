from django.contrib import admin
from .models import Member

# Register your models here

class AdminModel(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
        
admin.site.register(Member, AdminModel)