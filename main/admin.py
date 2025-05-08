from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at')
    
    list_display_links = ('name', 'email')

    search_fields = ('name', 'email', 'subject', 'message')

    list_filter = ('created_at',)

admin.site.register(Contact, ContactAdmin)
