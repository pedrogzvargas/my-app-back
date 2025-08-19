from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
from users.models import Profile

admin.site.register(Profile)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {
            'fields': ('second_name', 'second_last_name', )
        }),
    )

    # Campos al crear un usuario
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información adicional', {
            'classes': ('wide',),
            'fields': ('second_name', 'second_last_name', )
        }),
    )
