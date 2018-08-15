from django.contrib import admin
from .models import Services
# Register your models here.


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    '''Admin View for Services'''
    list_display =('name','description','status','type')