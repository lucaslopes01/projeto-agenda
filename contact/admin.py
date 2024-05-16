from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display =  'id','first_name', 'last_name', 'phone'
    ordering = 'id',
    search_fields = 'id','first_Name', 'last_name'
    list_max_show_all = 200 


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',

# Register your models here.
