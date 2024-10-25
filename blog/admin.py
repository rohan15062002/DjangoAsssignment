from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','author','published_at','is_published']
    search_fields=['title','author',]
    list_filter=['is_published',]

admin.site.register(Post,PostAdmin)