from django.contrib import admin
from .models import Author, Post, Tag

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name")


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("date",)
    list_display = ("title", "author", "date")
    list_filter = ("author", "tags", "date")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
