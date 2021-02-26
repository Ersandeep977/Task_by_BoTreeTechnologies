from django.contrib import admin
from app.models import Codeeditor, Category
# Register your models here.

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class Admincode(admin.ModelAdmin):
    list_display = ['title','description','category']

admin.site.register(Category, AdminCategory)
admin.site.register(Codeeditor, Admincode)

