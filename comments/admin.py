from django.contrib import admin

from .models import Comment

# Register your models here.


class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'body', 'created_on',)
                     
    ordering = ('name',)



admin.site.register(Comment, CommentAdmin)

