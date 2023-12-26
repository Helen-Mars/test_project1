from django.contrib import admin
from test_1.models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class PageAdmin(admin.ModelAdmin):
    list_play = ['title', 'category', 'url']


admin.site.register(Page, PageAdmin)


