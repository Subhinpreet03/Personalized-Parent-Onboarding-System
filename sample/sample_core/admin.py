from django.contrib import admin

# Register your models here.
from .models import Parent, Child, Blog


class ParentAdmin(admin.ModelAdmin):
    list_display = ["father_name", "mother_name", "parent_type"]
    search_fields = ["father_name", "mother_name", "email"]
    list_filter = ["parent_type"]


admin.site.register(Parent, ParentAdmin)
