from django.contrib import admin
from .models import Contact


# Customize admin site
admin.site.site_header = "AKNAN SITE"
admin.site.site_title = "AKNAN"
admin.site.index_title = "AKNAN"

from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at')

    