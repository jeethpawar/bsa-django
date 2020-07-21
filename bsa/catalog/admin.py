from django.contrib import admin

# Register your models here.
from .models import Genre, Author, Article





# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)





# Register the Admin classes for Book using the decorator
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genre)
