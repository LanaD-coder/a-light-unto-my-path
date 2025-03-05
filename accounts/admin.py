from django.contrib import admin
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "date_joined", "is_active")
    list_filter = ("is_active", "date_joined")
    search_fields = ("username", "email")

admin.site.unregister(User)
admin.site.register(User, UserAdmin)