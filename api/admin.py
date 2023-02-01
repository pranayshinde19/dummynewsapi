from django.contrib import admin
from .models import News
# Register your models here.

class Newsadmin(admin.ModelAdmin):
    list_display=['id','category','title','description','date','url','img']

admin.site.register(News,Newsadmin)