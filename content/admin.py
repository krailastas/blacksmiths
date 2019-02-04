from django.contrib import admin

from content.models import Category, Personal, Galery, MainPages, Book


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'keywords', 'is_active', 'order'
    )
    ordering = ('order', 'title')
    list_filter = ('is_active',)


class PersonalAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'fn', 'is_active', 'order', 'ln'
    )
    ordering = ('order', 'title')
    list_filter = ('is_active',)


class GaleryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'image', 'is_active', 'order'
    )
    ordering = ('order',)
    list_filter = ('is_active',)


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'phone', 'comment', 'created', 'status'
    )
    ordering = ('created', 'status')
    list_filter = ('created', 'status')


admin.site.register(Galery, GaleryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Personal, PersonalAdmin)
admin.site.register(MainPages)
admin.site.register(Book, BookAdmin)
