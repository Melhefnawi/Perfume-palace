from django.contrib import admin

from .models import Comment,Review, WishlistItem, ContactMessage

# Register your models here.


class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'body', 'created_on',)
                     
    ordering = ('name',)



admin.site.register(Comment, CommentAdmin)

class ReviewAdmin(admin.ModelAdmin):

    list_display = ('reviewer', 'item', 'rating', 'comment', 'created_at','reviews_count',)
                     
    ordering = ('reviewer',)



admin.site.register(Review, ReviewAdmin)


class WishlistAdmin(admin.ModelAdmin):

    list_display = ('user', 'product_name', 'product_description', 'added_at',)
                     
    ordering = ('user',)



admin.site.register(WishlistItem, WishlistAdmin)


class ContactMessageAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'subject', 'message','created_at',)
                     
    ordering = ('name',)



admin.site.register(ContactMessage, ContactMessageAdmin)

