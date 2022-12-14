from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    """Настройка отображения полей"""
    list_display = ('pk', 'username', 'role')
    list_editable = ('role',)


admin.site.register(User, UserAdmin)
