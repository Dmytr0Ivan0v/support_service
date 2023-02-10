from django.contrib import admin

_FIELDS: tuple[str, ...] = ("created_at", "updated_at")


class TimeStampReadonlyAdmin(admin.ModelAdmin):
    readonly_fields = _FIELDS
    list_display = _FIELDS
    list_filter = _FIELDS
    search_fields = _FIELDS
