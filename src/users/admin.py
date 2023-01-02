from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ["groups", "user_permissions"]
    readonly_fields = [
        "email",
        "password",
        "last_login",
        "is_staff",
        "is_active",
        "is_superuser",
    ]
    list_display = ["email", "first_name", "last_name", "role", "is_active"]
    list_filter = ["is_active", "role"]
    search_fields = ["email", "role"]
