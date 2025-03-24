from django.contrib import admin

# Register your models here.
from home.models import Settings, ContactMessage, Cuorses

class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'note', 'status']
    readonly_fields = ('name', 'phone', 'subject', 'message', 'ip')
    list_filter = ['status']

class CuorsesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title', 'description']


admin.site.register(Settings, SettingsAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Cuorses, CuorsesAdmin)