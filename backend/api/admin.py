from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Device, DevicePermission, Member


class MemberAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "phone",
        "is_staff",
        "is_active",
        "is_superuser",
    )
    search_fields = ("username", "email", "phone")
    ordering = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("email", "phone", "avatar")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "phone",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


admin.site.register(Member, MemberAdmin)
admin.site.register(Device)
admin.site.register(DevicePermission)
