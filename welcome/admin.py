# welcome/admin.py

from django.contrib import admin

from .models import PageView


class PageViewAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'timestamp']

admin.site.register(PageView, PageViewAdmin)
