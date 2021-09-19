from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.text import gettext_lazy as _
from import_export import admin as ie_admin

from apps.account_account import models as account_models


@admin.register(account_models.CustomUser)
class UserAdmin(DjangoUserAdmin, ie_admin.ImportExportModelAdmin):
    fieldsets = (
        (_("Main"), {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone",
                    "email",
                    "phone_verification_code",
                    "image",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "phone",
                    "dob",
                    "first_name",
                    "last_name",
                    "image",
                ),
            },
        ),
    )
    list_display = (
        "get_fullname",
        "id",
        "uuid",
        "phone",
        "is_staff",
        "date_joined",
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
        "phone",
    )
    ordering = ("email",)
    list_per_page = 200

    @staticmethod
    def get_fullname(obj):
        if obj.first_name or obj.last_name:
            return "{} {}".format(obj.first_name, obj.last_name)
        return "{}".format(obj.username)


@admin.register(account_models.Cashilok)
class CashilokAdmin(admin.ModelAdmin):
    list_display = ["id", "owner", "money"]


@admin.register(account_models.CashilokFill)
class CashilokFillAdmin(admin.ModelAdmin):
    list_display = ["id", "owner", "amount", "created"]


@admin.register(account_models.RateOfDriver)
class RateOfDriverAdmin(admin.ModelAdmin):
    list_display = ['id', 'on_trip', 'customer', 'rate']