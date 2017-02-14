from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
	list_display = ('title','Category','url','views')

# Register your models here.
admin.site.register(Category)
admin.site.register(Page, PageAdmin)