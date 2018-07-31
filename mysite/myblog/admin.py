from django.contrib import admin
from myblog.models import Post
from myblog.models import Category


class MembershipInline(admin.TabularInline):

    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):

    # Can only add categories to posts
    inlines = [
               MembershipInline,
               ]


class CategoryAdmin(admin.ModelAdmin):

    # If the following is uncommented,
    # you can also categorize posts from
    # the category page
    # inlines = [
    #            MembershipInline,
    #           ]
    exclude = ('posts', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
