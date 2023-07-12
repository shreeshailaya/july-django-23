from django.contrib import admin
from .models import BlogContent

# Register your models here.

@admin.register(BlogContent)
class BlogsContent(admin.ModelAdmin):
    search_fields = ['title', 'author']
    list_filter = ['author']
    list_display =[ 'title','author']
