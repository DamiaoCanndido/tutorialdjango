from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)
class PostAdimin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)}
